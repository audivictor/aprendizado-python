# 1. lista-compras

Programa básico de terminal para gerenciar uma lista de compras, com menu de três opções: incluir, apagar e listar itens.

Como funciona:

- Um loop principal exibe o menu até o usuário escolher uma opção válida.
- "Incluir" abre outro loop que pede itens um por um até o usuário indicar que não quer adicionar mais nada.
- "Apagar" mostra a lista numerada e remove o item pelo índice digitado.
- "Listar" exibe todos os itens já adicionados.

Usei tratamento de erros para evitar que o programa quebre se o usuário digitar um índice inválido ao apagar.
Além de validações para impedir itens vazios e opções de menu não reconhecidas.
