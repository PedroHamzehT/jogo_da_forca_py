import random


def velocidade_media(distancia, tempo):
    velocidade_media = divisao(distancia, tempo)
    return velocidade_media


def soma(numero1, numero2):
    return numero1 + numero2


def subtracao(numero1, numero2):
    return numero1 - numero2


def multiplicacao(numero1, numero2):
    return numero1 * numero2


def divisao(numero1, numero2):
    return numero1 / numero2


def calculadora(numero1, numero2):
    return soma(numero1, numero2), subtracao(numero1, numero2), multiplicacao(numero1, numero2), divisao(numero1, numero2)


print('{} \n'.format(calculadora(random.randint(1, 100), random.randint(1, 100))))
print('{} \n'.format(calculadora(random.randint(1, 100), random.randint(1, 100))))
print('{} \n'.format(calculadora(random.randint(1, 100), random.randint(1, 100))))
print('{} \n'.format(calculadora(random.randint(1, 100), random.randint(1, 100))))
print('{} \n'.format(calculadora(random.randint(1, 100), random.randint(1, 100))))
