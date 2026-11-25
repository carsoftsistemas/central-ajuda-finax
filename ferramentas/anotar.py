"""Gera as imagens marcadas do manual (mesmo padrão visual dos vídeos).

Uso:  python3 ferramentas/anotar.py ferramentas/imagens.json

Para cada imagem do JSON:
  - "print": caminho do print HD (1920x1080). Se não existir, desenha uma
    tela provisória com os "campos" listados, marcada como PROVISÓRIA.
  - "marcas": [{"n": 1, "box": [x, y, w, h]}] em pixels do print 1920x1080.
    Desenha o retângulo laranja e o círculo verde-água numerado.
  - "recorte": [x, y, w, h] opcional, para mostrar só a área relevante.
  - "saida": caminho do PNG dentro de docs/img/.
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

VERDE, LARANJA, PRETO = (58, 163, 165), (242, 120, 34), (26, 26, 18)
F = "/usr/share/fonts/opentype/inter/Inter-%s.otf"
def fonte(peso, tam):
    try: return ImageFont.truetype(F % peso, tam)
    except OSError: return ImageFont.load_default()

def tela_provisoria(spec):
    W, H = 1920, 1080
    im = Image.new("RGB", (W, H), (226, 236, 246))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 46], fill=(40, 84, 130))
    d.text((18, 10), "Finax  —  " + spec.get("tela", ""), font=fonte("SemiBold", 22), fill="white")
    # barra de botões
    d.rectangle([0, 46, W, 118], fill=(245, 248, 252))
    for c in spec.get("campos", []):
        x, y, w, h = c["box"]
        tipo = c.get("tipo", "campo")
        if tipo == "botao":
            d.rounded_rectangle([x, y, x + w, y + h], 6, fill=(255, 255, 255), outline=(150, 165, 185), width=2)
            tw = d.textlength(c["rotulo"], font=fonte("Medium", 20))
            d.text((x + (w - tw) / 2, y + h / 2 - 12), c["rotulo"], font=fonte("Medium", 20), fill=PRETO)
        elif tipo == "janela":
            d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255), outline=(40, 84, 130), width=3)
            d.rectangle([x, y, x + w, y + 38], fill=(40, 84, 130))
            d.text((x + 12, y + 7), c["rotulo"], font=fonte("SemiBold", 19), fill="white")
        elif tipo == "texto":
            d.text((x, y), c["rotulo"], font=fonte("SemiBold", 22), fill=c.get("cor_rgb") and tuple(c["cor_rgb"]) or PRETO)
        else:
            d.text((x, y - 28), c["rotulo"], font=fonte("Medium", 19), fill=(55, 65, 80))
            d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255), outline=(150, 165, 185), width=2)
            if c.get("valor"):
                d.text((x + 10, y + h / 2 - 12), c["valor"], font=fonte("Regular", 20), fill=PRETO)
            if c.get("lupa"):
                d.ellipse([x + w + 10, y + 6, x + w + 30, y + 26], outline=(60, 80, 110), width=3)
                d.line([x + w + 27, y + 23, x + w + 36, y + 32], fill=(60, 80, 110), width=3)
    return im

def selo(im):
    d = ImageDraw.Draw(im); W, H = im.size
    t = "IMAGEM PROVISÓRIA · será trocada pelo print real do Finax"
    fs = fonte("SemiBold", 18); tw = d.textlength(t, font=fs)
    d.rounded_rectangle([W - tw - 44, H - 50, W - 14, H - 14], 8, fill=(255, 244, 214), outline=(220, 170, 60), width=2)
    d.text((W - tw - 29, H - 44), t, font=fs, fill=(120, 80, 0))

def marcar(im, marcas):
    d = ImageDraw.Draw(im)
    r = 15
    for m in marcas:
        x, y, w, h = m["box"]; p = 5
        d.rounded_rectangle([x - p, y - p, x + w + p, y + h + p], 10, outline=LARANJA, width=4)
        # círculo no canto superior direito (padrão) ou à esquerda/direita ("lado")
        lado = m.get("lado", "canto")
        if lado == "esq": cx, cy = x - p - r - 8, y + h / 2
        elif lado == "dir": cx, cy = x + w + p + r + 8, y + h / 2
        else: cx, cy = x + w + p, y - p
        cx = min(max(cx, r + 4), im.width - r - 4); cy = max(cy, r + 4)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=VERDE, outline="white", width=3)
        t = str(m["n"]); f = fonte("Bold", 19); tw = d.textlength(t, font=f)
        d.text((cx - tw / 2, cy - 12), t, font=f, fill="white")
    return im

def gerar(spec, base):
    caminho = spec.get("print")
    if caminho and os.path.exists(os.path.join(base, caminho)):
        im = Image.open(os.path.join(base, caminho)).convert("RGB")
        provisoria = False
    else:
        im = tela_provisoria(spec); provisoria = True
    im = marcar(im, spec.get("marcas", []))
    if spec.get("recorte"):
        x, y, w, h = spec["recorte"]; im = im.crop((x, y, x + w, y + h))
    if provisoria: selo(im)
    if im.width > 1600:
        im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
    saida = os.path.join(base, spec["saida"])
    os.makedirs(os.path.dirname(saida), exist_ok=True)
    im.save(saida, optimize=True)
    print("ok", spec["saida"], im.size)

if __name__ == "__main__":
    arq = sys.argv[1]
    base = os.path.dirname(os.path.dirname(os.path.abspath(arq)))
    for s in json.load(open(arq, encoding="utf-8")):
        gerar(s, base)
