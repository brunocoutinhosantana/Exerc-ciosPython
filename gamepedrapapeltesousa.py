from random import randint
from time import sleep
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
item = ['Pedra', 'Papel', 'Tesoura']
jogador = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if jogador == 0:
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('COMPUTADOR VENCEU')
    elif computador == 2:
        print('JOGADOR VENCEU')
elif jogador == 1:
    if computador == 0:
        print('JOGADOR VENCEU')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('COMPUTADOR VENCEU')
elif jogador == 2:
    if computador == 0:
        print('COMPUTADOR VENCEU')
    elif computador == 1:
        print('JOGADOR VENCEU')
    elif computador == 2:
        print('EMPATE')
else:
    print('OPÇÃO INVÁLIDA')
print('=-' * 12)
print('Computador jogou {}'.format(item[computador]))
print('Jogador jogou {}'.format(item[jogador]))
print('=-' * 12)




