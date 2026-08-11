# =================== Lista de compras ===================

import os

comprar = []

def LIMPAR_TERMINAL():
    os.system("cls")

print("Selecione uma das opções: ")

while True:
    print("[I]ncluir    [A]pagar    [L]istar")
    menu = input("").strip().lower()

    if menu.isalpha():
        if menu == "i":
            while True:
                LIMPAR_TERMINAL()
                print('Digite o que você quer incluir')
                adicionar = input("").strip()
                if adicionar == "":
                    print("Você não digitou nada.")
                    continue

                comprar.append(adicionar)

                LIMPAR_TERMINAL()
                print("Quer incluir algo a mais?")
                print("[S]im    [N]ão")

                confirmar = input("").strip().lower()

                if confirmar == "s":
                    continue

                else:
                    LIMPAR_TERMINAL()
                    break

        elif menu == "a":
            if comprar == []:
                LIMPAR_TERMINAL()
                print("Não há itens na lista para apagar.")
                continue

            else:
                LIMPAR_TERMINAL()
                while True:
                    for indice, item in enumerate(comprar):
                        print(f"{indice} - {item}")

                    print("Digite o índice do item que você quer apagar")
                    try:
                        apagar = int(input("").strip())

                        if 0 <= apagar < len(comprar):
                            del comprar[apagar]

                            LIMPAR_TERMINAL()
                            print("Quer apagar mais algo?")
                            print("[S]im    [N]ão")

                            confirmar = input("").strip().lower()

                            if confirmar == "s":
                                LIMPAR_TERMINAL()
                                continue

                            else:
                                LIMPAR_TERMINAL()
                                break

                        else:
                            print("Digite um número que corresponda a um índice da lista.")

                    except (ValueError, IndexError):
                        LIMPAR_TERMINAL()
                        print("Digite um dos índices exibidos na lista.")
                        continue

        elif menu == "l":
            if comprar == []:
                LIMPAR_TERMINAL()
                print("Não há itens na lista para exibir.")
                continue

            else:
                LIMPAR_TERMINAL()
                for item in comprar:
                    print(item)

                continue

        else:
            LIMPAR_TERMINAL()
            print("Opção não reconhecida.")
            continue

    else:
        LIMPAR_TERMINAL()
        print("Digite uma das opções exibidas no menu.")
        continue
