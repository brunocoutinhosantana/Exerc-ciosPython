n = int(input('Quantos elementos da sequencia de fibonacci você quer mostrar? '))
primeiro = 0
segundo = 1
cont = 1
while cont <= n:

    print('{} -> {} -> {}'.format(primeiro, segundo, (primeiro + segundo)), end='')
    cont += 1

