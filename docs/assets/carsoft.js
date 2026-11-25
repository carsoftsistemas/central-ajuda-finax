// Clique na imagem da tela para ampliar
document.addEventListener("click", function (e) {
  var img = e.target.closest && e.target.closest("figure.tela img");
  if (img) {
    var box = document.createElement("div");
    box.className = "cs-zoom";
    var big = document.createElement("img");
    big.src = img.src; big.alt = img.alt;
    box.appendChild(big);
    box.addEventListener("click", function () { box.remove(); });
    document.body.appendChild(box);
    return;
  }
});
document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") document.querySelectorAll(".cs-zoom").forEach(function (b) { b.remove(); });
});
