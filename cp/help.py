def escreva(texto):
    tamanho = len(texto) + 4
    print("~" * tamanho)
    print(f"  {texto}")
    print("~" * tamanho)


def pyhelp(comando):
    help(comando)


def default_loop():
    while True:
        escreva("Sistema de ajuda PyHELP")
        funcao_ou_lib = input("Função ou Biblioteca > ")

        if funcao_ou_lib[0].lower() == "f":
            break
        else:
            # escreva(f"Acessando o manual do comando {funcao_ou_lib}")
            # sleep(1)
            pyhelp(funcao_ou_lib)


default_loop()