def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número interio válido')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            break
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número real válido')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            break
        else:
            return n


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
f = leiaFloat('Digite um número real: ')
print(f'Você digitou o número {f}')
