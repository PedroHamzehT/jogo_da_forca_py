import pdb
import random

def boas_vindas():
    print('*' * 31)
    print('* Bem vindo ao jodo da Forca! *')
    print('*' * 31)

def escolha_a_dificuldade():
    print('***************************************')
    print('*   Escolha o nivel de dificuldade:   *')
    print('*                                     *')
    print('* 1 - Facil | 2 - Medio | 3 - Dificil *')
    print('***************************************')
    difficult = int(input())
    if(difficult == 1):
        tries = 20
        print('dificuldade escolhida: Facil')
    elif(difficult == 2):
        tries = 10
        print('Dificuldade escolhida: Medio')
    else:
        tries = 5
        print('Dificuldade escolhida: Dificil')
    
    return tries

def gerar_frutas():
    fruits = []
    with open('frutas.txt', 'r') as file:
        for line in file.readlines():
            fruits.append(line.rstrip())
    
    return fruits

def escolher_palavra_secreta(fruits):
    random_index = random.randint(0, len(fruits)+1)
    secret_word = fruits[random_index]
    return secret_word

def jogar():
    print('')

    tries = escolha_a_dificuldade()

    fruits = gerar_frutas()

    while True:
        secret_word = escolher_palavra_secreta(fruits)
        discovered_letters = []
        for letter in secret_word:
            discovered_letters.append('_')

        word_discovered = ''.join(discovered_letters)
        discovered = word_discovered == secret_word
        user_tries = 0
        letters_tried = []
        while not discovered:
            if user_tries > tries:
                break
            print('***********************************************************')
            print(
                '* Total de tentativas: {}, Total de tentativas falhas: {} *'.format(tries, user_tries))
            print('***********************************************************')
            user_letter_try = input('Tente uma letra: ')
            if (user_letter_try in letters_tried):
                print('Voce ja tentou essa letra!')
                continue
            letters_tried.append(user_letter_try)
            if(len(user_letter_try) > 1):
                print('Insira somente uma letra!')
                continue
            if(user_letter_try in list(secret_word)):
                print('Acertou!')
            else:
                user_tries += 1
                print('Errou!')
                print('\n')
                print('*' * 21)
                print('* Dica: Eh uma fruta *')
                print('*' * 21)
                print('\n')
            index = 0
            for letter in secret_word:
                if(user_letter_try.upper() == letter.upper()):
                    discovered_letters[index] = user_letter_try.upper()
                index = index + 1
            print('Letras que ja foram:')
            letters_tried_in_string = ' '.join(letters_tried)
            print(letters_tried_in_string)
            word_discovering = ' '.join(discovered_letters)
            print(word_discovering)
            word_discovered = ' '.join(discovered_letters)
            discovered = word_discovered.upper() == secret_word.upper()
            print('\n')
            print('*' * 50)
            print('\n')

        if(discovered):
            print('Parabens voce ganhou o jogo a palavra certa era {}!'.format(
                secret_word.upper()))
        else:
            print('Voce perdeu seu boneco foi enforcado, a palavra era: {}'.format(
                secret_word.upper()))
        play_again = input('Quer jogar novamente? (S/N): ')
        if(play_again.upper() is 'N' or 'NAO' or 'Não'):
            break
