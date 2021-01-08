# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
import time
import random
print('Jogo da Adivinhação!')
time.sleep(0.5)
print('*-*' * 24)
time.sleep(1)
print('Irei pensar em um número entre 0 e 10 e você terá que adivinhar!')
time.sleep(0.5)
print('*-*' * 24)
time.sleep(0.5)
print('Pensando...')
time.sleep(1.5)
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ne = random.choice(n)
eu = int(input('Digite seu palpite de 0 à 10: '))
count = 1
maior = ne
menor = ne
while eu != ne:
    if eu > ne:
        print('Menos... Tente novamente!')
    if eu < ne:
        print('Mais... Tente novamente!')
    eu = int(input('Digite seu palpite: '))
    count += 1
print('Parabéns você acertou! Você tentou {} vezes!'.format(count))
