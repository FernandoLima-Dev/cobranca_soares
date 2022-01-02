def get_info_usuario_int(msg):
    """
    -> captura teclado e retorna numero em int
    :param msg: msg a ser apreentada na tela para usuario
    :return: numero formatado em int
    Desenvoldo por Fernando-Dev
    """
    while True:
        try:
            get_usuario = int(input(msg))
            return get_usuario

        except ValueError as err:
            print('Nao foi digitado um numero por favor tente novamente...')

if __name__ == '__main__':
    print(f'teste retorno {get_info_usuario_int("teste.: ")}')