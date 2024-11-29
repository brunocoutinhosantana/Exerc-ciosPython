print('-'*30)
print('MENU PRINCIPAL'.center(30))
print('-'*30)
print('1 - Ver pessoas cadastradas')
print('2 - Cadastrar nova Pessoa')
print('3 - Sair do Sistema')
print('-'*30)
def opcao(n):
    while True:
        try:
            n = int(input('Sua opção:'))
        except:
            print('ERRO: por favor, digite um número inteiro válido.')
        else:
            while not