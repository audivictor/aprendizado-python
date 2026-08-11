# 2. validador-cpf

Programa que valida um CPF conferindo se os dois últimos dígitos (dígitos verificadores) batem com o resultado esperado pelo algoritmo oficial.

Como funciona: 

- O usuário digita o CPF, o programa remove pontos e traços e confere se sobraram exatamente 11 números.
- Depois calcula o primeiro dígito verificador, conforme padrão brasileiro, multiplicando os 9 primeiros números por pesos decrescentes (10 a 2), somando o resultado e aplicando o resto da divisão por 11.
- O segundo dígito segue a mesma lógica, usando os 10 primeiros números (os 9 originais + o primeiro dígito calculado) com pesos de 11 a 2.
- Se os dois dígitos calculados baterem com os informados, o CPF é considerado válido.

Usei um bloco de loop pra permitir várias tentativas sem reiniciar o programa.
E também validações de entrada pra rejeitar CPFs com letras ou tamanho incorreto antes de tentar o cálculo.
