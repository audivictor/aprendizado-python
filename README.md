# Aprendizado em Python

Este repositório reúne exercícios e pequenos projetos que venho desenvolvendo durante meus estudos de Python
através de cursos e da graduação em Ciência da Computação.

É um material em constante evolução, atualizado conforme avanço nos estudos

> **Nota:** os projetos estão numerados em ordem cronológica. Como este 
> repositório é atualizado conforme avanço nos estudos, é esperado que a 
> qualidade do código melhore a cada novo projeto adicionado.


## Projetos

### 1. lista-compras
Programa básico de terminal para gerenciar uma lista de compras, com menu de três opções: incluir, apagar e listar itens.

Como funciona:
- Um loop principal exibe o menu até o usuário escolher uma opção válida.
- "Incluir" abre outro loop que pede itens um por um até o usuário indicar que não quer adicionar mais nada.
- "Apagar" mostra a lista numerada e remove o item pelo índice digitado.
- "Listar" exibe todos os itens já adicionados.

Usei tratamento de erros para evitar que o programa quebre se o usuário digitar um índice inválido ao apagar
Além de validações para impedir itens vazios e opções de menu não reconhecidas.


### 2. validador-cpf
Programa que valida um CPF conferindo se os dois últimos dígitos (dígitos verificadores) batem com o resultado esperado pelo algoritmo oficial.

Como funciona: 
- O usuário digita o CPF, o programa remove pontos e traços e confere se sobraram exatamente 11 números.
- Depois calcula o primeiro dígito verificador, conforme padrão brasileiro, multiplicando os 9 primeiros números por pesos decrescentes (10 a 2), somando o resultado e aplicando o resto da divisão por 11.
- O segundo dígito segue a mesma lógica, usando os 10 primeiros números (os 9 originais + o primeiro dígito calculado) com pesos de 11 a 2.
- Se os dois dígitos calculados baterem com os informados, o CPF é considerado válido.

Usei um bloco de loop pra permitir várias tentativas sem reiniciar o programa.
E também validações de entrada pra rejeitar CPFs com letras ou tamanho incorreto antes de tentar o cálculo.

