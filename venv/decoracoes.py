
def titulo(msg):
    """
    -> decora uma caixa para estilizar o titulo
    :param msg: titulo que sera mostrado dentro caixa
    :return: none
    Desenvoldo por Fernando-Dev
    """

    #linha 1
    print('+--', end='')
    print('-' * len(msg), end='')
    print('--+')

    # linha 2
    print('|  ', end='')
    print(" " * len(msg), end='')
    print('  |')

    # linha 3
    print('|  ', end='')
    print(msg, end='' )
    print('  |')

    # linha 4
    print('|  ', end='')
    print(" " * len(msg), end='')
    print('  |')

    # linha 5
    print('+--', end='')
    print('-' * len(msg), end='')
    print('--+')

    print()

if __name__ == '__main__':
    titulo('steelers sera qua vai consguir playoffs')
    help(titulo)