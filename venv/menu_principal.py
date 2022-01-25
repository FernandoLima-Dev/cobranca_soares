from utilitario import get_info_usuario_int

def menu_start():
    print('Menu Cobranca...')
    while True:
        get_menu = get_info_usuario_int('\nDigite uma das opçoes abaixo sendo:'
                                         '\n1 - Cliente'
                                         '\n2 - Inserir nota'
                                         '\n3 - Listar Todos Clientes'
                                         '\n4 - Listar Contas Vencidas  '
                                         '\n5 - sair...')

        # opcao 1 menu
        if get_menu == 1:
            pass
            break

        # opcao 2 menu
        elif get_menu == 2:
            pass
            break

        # opcao 3 menu
        elif get_menu == 3:
            pass
            break

        # opcao 4 menu
        elif get_menu == 4 :
            pass
            break

        # opcao 4 menu
        elif get_menu == 5:
            pass
            break

        # retorna para apresentacao do menu novamente
        else:
            print('Opção Errada...')



if __name__ == '__main__':
    menu_start()