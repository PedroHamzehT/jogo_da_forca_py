def teste_args(*args):
    for arg in args:
        print('arg: ', arg)


argumentos = ('Argumento1', 'Argumento2', 'Argumento3')
teste_args(*argumentos)


def teste_kwargs(**kargs):
    for chave, valor in kargs.items():
        print('Chave: {}; Valor: {}'.format(chave, valor))


argumentos_chaves = {'arg1': 'Argumento1',
                     'arg2': 'Argumento2', 'arg3': 'Argumento3'}
teste_kwargs(**argumentos_chaves)
