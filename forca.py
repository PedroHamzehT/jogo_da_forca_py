import pdb
import random

print('*' * 31)
print('* Bem vindo ao jodo da Forca! *')
print('*' * 31)

print('')

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

fruits = ['Abacate', 'Abacaxi', 'Abiu', 'Abricó', 'Açaí', 'Acerola', 'Akee', 'Alfarroba', 'Ameixa', 'Amêndoa', 'Amora', 'Ananás', 'Anona', 'Araçá', 'Arando', 'Araticum', 'Atemoia', 'Avelã', 'Babaco', 'Babaçu', 'Bacaba', 'Bacuri', 'Bacupari', 'Banana', 'Baru', 'Bergamota', 'Biribá', 'Buriti', 'Butiá', 'Cabeludinha', 'Cacau', 'Cagaita', 'Caimito', 'Cajá', 'Caju', 'Calabaça', 'Calabura', 'Calamondin', 'Cambucá', 'Cambuci', 'Camu-camu', 'Caqui', 'Carambola', 'Carnaúba', 'Castanha', 'Castanha do Pará', 'Cereja', 'Ciriguela', 'Ciruela', 'Coco', 'Cranberry', 'Cupuaçu', 'Damasco', 'Dekopon', 'Dendê', 'Dióspiro', 'Dovyalis', 'Durião', 'Embaúba', 'Embaubarana', 'Engkala', 'Escropari', 'Esfregadinha', 'Figo', 'Framboesa', 'Fruta-do-conde', 'Fruta-pão', 'Feijoa', 'Figo-da-índia', 'Fruta-de-cedro', 'Fruta-de-lobo', 'Fruta-do-milagre', 'Fruta-de-tatu', 'Gabiroba', 'Glicosmis', 'Goiaba', 'Granadilla', 'Gravatá', 'Graviola', 'Groselha', 'Grumixama', 'Guabiju', 'Guabiroba', 'Guaraná', 'Hawthorn', 'Heisteria', 'Hilocéreo', 'Ibacurupari', 'Ilama', 'Imbe', 'Imbu', 'Inajá', 'Ingá', 'Inharé', 'Jabuticaba', 'Jaca', 'Jambo', 'Jambolão', 'Jamelão', 'Jaracatiá', 'Jatobá', 'Jenipapo', 'Jerivá', 'Juá', 'Jujuba', 'Kabosu', 'Karité', 'Kiwi', 'Kumquat', 'Fruta com L', 'Langsat', 'Laranja', 'Lichia', 'Lima', 'Limão', 'Longan', 'Lucuma', 'Fruta com M', 'Mabolo', 'Maçã', 'Macadâmia', 'Macaúba', 'Mamão', 'Mamey', 'Mamoncillo', 'Maná-cubiu', 'Manga', 'Mangaba', 'Mangostão', 'Maracujá', 'Marang', 'Marmelo', 'Marolo', 'Marula', 'Massala', 'Melancia', 'Melão', 'Meloa', 'Mexerica', 'Mirtilo', 'Morango', 'Murici', 'Fruta com N', 'Naranjilla', 'Nectarina', 'Nêspera', 'Noni', 'Noz', 'Noz-pecã', 'Noz-macadâmia', 'Oiti', 'Oxicoco', 'Orangelo', 'Pera', 'Pêssego', 'Pitanga', 'Pinha', 'Pitaia', 'Pitomba', 'Pitangatuba', 'Pindaíba', 'Pequi', 'Pequiá', 'Physalis', 'Pulasan', 'Pomelo', 'Pupunha', 'Puçá', 'Patauá', 'Pajurá', 'Pixirica', 'Pistache', 'Quina', 'Quiuí', 'Fruta com R', 'Romã', 'Rambai', 'Rambutão', 'Rukam', 'Saguaraji', 'Salak', 'Santol', 'Sapota', 'Sapoti', 'Sapucaia', 'Saputá', 'Seriguela', 'Sorvinha', 'Tangerina', 'Tamarindo', 'Tâmara', 'Toranja', 'Tucumã', 'Taiuva', 'Tapiá', 'Tarumã', 'Tangor', 'Tucujá', 'Uva', 'Umbu', 'Uvaia', 'Uchuva', 'Umê', 'Uxi', 'Veludo', 'Vergamota', 'Wampi', 'Xixá', 'Yamamomo', 'Yuzu', 'Zimbro']
while True:
    random_index = random.randint(0, len(fruits))
    secret_word = fruits[random_index]
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
        print('* Total de tentativas: {}, Total de tentativas falhas: {} *'.format(tries, user_tries))
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
        word_discovering = ''.join(discovered_letters)
        print(word_discovering)
        word_discovered = ''.join(discovered_letters)
        discovered = word_discovered.upper() == secret_word.upper()
        print('\n')
        print('*' * 50)
        print('\n')

    if(discovered):
        print('Parabens voce ganhou o jogo a palavra certa era {}!'.format(secret_word.upper()))
    else:
        print('Voce perdeu seu boneco foi enforcado, a palavra era: {}'.format(secret_word.upper()))
    play_again = input('Quer jogar novamente? (S/N): ')
    if(play_again.upper() is 'N' or 'NAO' or 'Não'):
        break
