# ========== PRIMEIRO DIGITO ==========

while True:
    print("Digite o número do seu CPF:")
    cpf_enviado = input("").strip()


    if "." in cpf_enviado or "-" in cpf_enviado or " " in cpf_enviado:
        cpf_enviado = cpf_enviado.replace(".", "")
        cpf_enviado = cpf_enviado.replace("-", "")
        cpf_enviado = cpf_enviado.replace(" ", "")
        cpf_enviado = cpf_enviado.strip()

    if len(cpf_enviado) != 11:
        print("O CPF deve conter apenas 11 números") 
        continue

    elif not cpf_enviado.isdigit():
        print("O CPF enviado deve conter apenas números, '.' e '-'")
        continue

    cpf_para_calculo = cpf_enviado[:9]
    multiplicador = 10
    soma_vezes10_v1 = 0

    print(f"Os 9 primeiros números do CPF são: '{cpf_para_calculo}'")

    for digito in cpf_para_calculo:
        soma_vezes10_v1 += int(digito) * multiplicador

        multiplicador -= 1

    primeiro_digito = soma_vezes10_v1 * 10 % 11

    if primeiro_digito > 9:
        primeiro_digito = 0

    print(f"- O 1º dígito calculado do CPF é {primeiro_digito}")

    # ========== SEGUNDO DIGITO ==========
    cpf_incompleto = cpf_para_calculo + str(primeiro_digito)

    multiplicador = 11
    soma_vezes10_v2 = 0

    for numeros in cpf_incompleto:
        soma_vezes10_v2 += (int(numeros) * multiplicador)

        multiplicador -= 1

    segundo_digito = soma_vezes10_v2 * 10 % 11

    if segundo_digito > 9:
        segundo_digito = 0

    print(f"- O 2º dígito calculado do CPF é {segundo_digito}")

    cpf_calculado = cpf_incompleto + str(segundo_digito)

    print(f"O CPF calculado é {cpf_calculado}")
    print("")


    if cpf_calculado == cpf_enviado:
        print("CPF VÁLIDO")
        break

    else:
        print("CPF INVÁLIDO")
        break
