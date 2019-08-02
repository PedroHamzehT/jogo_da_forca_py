import pdb

# Estrutura de dados Ex 1
any_list = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print('O maior valor da lista eh: {}'.format(max(any_list)))
print('*' * 20)
print('O menor valor valor da lista eh: {}'.format(min(any_list)))
print('*' * 20)
ocurrency_of_first_number = 0
for element in any_list:
    if element == any_list[0]:
        ocurrency_of_first_number += 1
print('O primeiro numero da lista({}) apareceu {} vezes'.format(any_list[0], ocurrency_of_first_number))
print('*' * 20)
list_average = sum(any_list)/len(any_list)
print('Media dos elemtos da lista: {}'.format(round(list_average, 2)))
print('*' * 20)
negative_numbers = []
for element in any_list:
    if(element < 0):
        negative_numbers.append(element)
sum_of_negative_numbers = sum(negative_numbers)
print('A soma dos numeros negativos deu: {}'.format(sum_of_negative_numbers))

# Estrutura de dados Ex 2
print('*' * 50)
user_datas = []
user_datas.append(input('Digite seu nome por favor: '))
user_datas.append(input('Digite seu sobrenome por favor: '))
user_datas.append(input('Digite sua idade por favor: '))
for data in user_datas:
    print(data)

# Estrutura de dados Ex 3
print('*' * 50)
user_grades = []
user_grades.append(float(input('Digite a primeira nota: ')))
user_grades.append(float(input('Digite a segunda nota: ')))
user_grades.append(float(input('Digite a terceira nota: ')))
user_grades.append(float(input('Digite a quarta nota: ')))
user_average = sum(user_grades)/len(user_grades)
print('A media do aluno foi: {}'.format(round(user_average, 2)))

# Estrutura de dados Ex 4 e Ex 5
print('*' * 50)
users = []
while True:
    name = input('Digite o seu nome por favor: ')
    age = input('Digite a sua idade por favor: ')
    city = input('Digite a cidade onde mora por favor: ')
    users.append({'name': name, 'age': age, 'city': city})
    if(input('Quer adicionar outro usuario? (S/N) ').upper() == 'N'):
        break
for user in users:
    print('{}: {}'.format('nome', user['name']))
    print('{}: {}'.format('idade', user['age']))
    print('{}: {}'.format('cidade', user['city']))
    print('*' * 10)
