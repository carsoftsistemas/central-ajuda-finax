---
title: Mensagens do sistema
atualizado: 24/11/2026
versao: 8.3.8.7
---

# Mensagens do sistema

Apareceu uma mensagem no Finax? Use ++ctrl+f++ ou a busca do site para encontrar o texto.

## Contas a Pagar

| Mensagem | Causa | Como resolver |
|---|---|---|
| A Conta informada não foi encontrada ou não está ativada! | Conta Financeira em branco ou inexistente | Preencha a Conta Financeira. Se a lista estiver vazia, cadastre uma conta antes |
| A pesquisa não pode localizar os dados porque a tabela encontra-se vazia! | A lista de pesquisa não tem cadastros | Cadastre o item primeiro (ex.: Conta Financeira) |
| Campo "Conta Débito" deve ser preenchido! | Conta Débito vazia | Escolha a conta contábil pela lupa |
| Campo Historico Padrão deve ser preenchido! | Histórico vazio | Escolha o histórico pela lupa |
| Campo Descrição deve ser preenchido | Item sem descrição | Digite a descrição do item ([Itens](pagar/itens.md)) |
| A data informada refere-se a um dia não útil! | Vencimento em sábado, domingo ou feriado | É apenas um aviso; ajuste a data se quiser |
| Título desbaixado com sucesso! | A baixa foi retirada | Clique em OK |
| Registro clonado com sucesso! Nº (xxxx)... | O clone foi criado | Clique em OK para abrir o novo título |
| Confirma a retirada do título... da baixa? | Retirar da Baixa, na Baixa Múltipla | Sim retira a linha; Aplicar Filtro traz de volta |
| Deseja baixar os registros que contenham os dados de baixa preenchidos? | Efetuar baixa, na Baixa Múltipla | Sim para baixar |
| Títulos que já possuam pelo menos uma parcela baixada não podem ser agrupados! | Consolidar com título já pago | Selecione só títulos totalmente em aberto |
| Não há Provisões a gerar para as datas selecionadas... | Não existe matriz de provisão | Cadastre a matriz com vencimento dd/01/1001 ([Provisões](pagar/provisoes.md)) |
| Confirma a geração de provisões? | Gerar, na tela de Provisões | Sim para gerar |
| Processo concluído com mensagens de aviso! | A geração de provisões terminou | Clique em OK e leia o log de operações |
| Encontrado(s) (n) registro(s), Deseja excluir estes títulos? | Excluir Títulos, na tela de Provisões | Sim exclui as provisões do período; Não cancela |
| Deseja Excluir o Documento "nome do arquivo"? | Excluir, na janela Documentos | Sim remove o anexo; Não cancela |
| ISC ERROR CODE:335544343 ... GEN_ID_DOCUMENTO is not defined | Ajuste pendente no banco de dados | Clique em OK e avise o suporte da Carsoft |

## Geral

| Mensagem | Causa | Como resolver |
|---|---|---|
| Este Sistema já está em uso nesta máquina! | O Finax já está aberto neste computador | Use a janela que já está aberta |
