from utilitario import get_info_usuario_int

def menu_start():
    print('Menu Cobranca...')
    while True:
        get_menu = get_info_usuario_int('\nDigite uma das opçoes abaixo sendo:'
                                         '\n1 - Cadastrar Cliente'
                                         '\n2 - Inserir nota'
                                         '\n3 - Listar Clientes'
                                         '\n4 - Listar Contas Vencidas  ')

        if get_menu == 1:       #opcao 1 menu
            pass
            break


        elif get_menu == 2:     #opcao 2 menu
            pass
            break

        elif get_menu == 3:     #opcao 3 menu
            pass
            break

        elif get_menu == 4 :    #opcao 4 menu
            pass
            break

        else:                   #retorna para apresentacao do menu novamente
            print('Opção Errada...')



if __name__ == '__main__':
    menu_start()