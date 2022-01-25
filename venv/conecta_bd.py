import psycopg2 as bd

def conect_bd(sql):
    with bd.connect(host='localhost', database='cobranca', user='postgres', password='root') as conexao_bd:
        try:
            cursor = conexao_bd.cursor()
            cursor.execute(sql)
            conexao_bd.commit()
        except Exception as err:
            if err.__class__.__name__ == 'UniqueViolation':
                return 'Erro na operacao de insercao'

            print(f'Erro -> {err.__class__.__name__}')

        print(f'teste status msg -> {cursor.statusmessage}')
        status_bd = cursor.statusmessage

        if 'INSERT' == status_bd:
            print('Dados Inseridos com Sucesso...')
            return

        elif 'DELETE' == status_bd:
            print('Deletado(a) com Sucesso...')
            return

        elif 'DELETE 0' == status_bd:
            print('Cliente Nao encontrado...')
            return

        return cursor.fetchall()

def listar_clientes():
    list_clientes = conect_bd('select * from cliente')
    print(f'{":.Codigo.:":12}{":.Nome.:":30}{":.Endereço.:":40}{":.Bairro.:":15}{":.CEP.:":15}{":.Telefone.:":20}{":.Whatsapp.:":20}{":.Responsavel.:":35}')
    for ls_cliente in list_clientes:
        print(f'{ls_cliente[0]:^12}{ls_cliente[1]:30}{ls_cliente[2]:40}{ls_cliente[3]:15}{ls_cliente[4]:15}{ls_cliente[5]:20}{ls_cliente[6]:20}{ls_cliente[7]:35}')

def listar_notas():
    list_notas = conect_bd("select cod_cliente,numero_nota, to_char(data_nota, 'DD/MM/YYYY'), valor_nota from nota")
    print(f'{"Cliente":10}{"Nº Nota":10}{"Data":15}{"Valor":10}')
    for ls_notas in list_notas:
        print(f'{ls_notas[0]:^10}{ls_notas[1]:<10}{ls_notas[2]:<15}R$ {ls_notas[3]:<10.2f}')

def listar_nota_cliente(codigo_cliente):
    notas_cliente = conect_bd(f"select cliente.cod_cliente, nome, numero_nota, to_char(data_nota, 'DD/MM/YY'), valor_nota from cliente, nota where cliente.cod_cliente = nota.cod_cliente and nota.cod_cliente = {codigo_cliente}")
    print(f"O cliente selecionado foi.: {notas_cliente[0][1]}, Codigo.: {notas_cliente[0][0]}"
          f"\nsegue relaçao de notas do mesmo")
    print(f'{"Nota":10}{"Data":15}{"Valor":10}')

    for nt_cliente in notas_cliente:
        print(f'{nt_cliente[2]:<10}{nt_cliente[3]:<15}R$ {nt_cliente[4]:<10.2f}')

def adiconar_nota(cod_cliente,data_nota, numero_nota, valor_nota):
        retorno = conect_bd(f"insert into nota values({cod_cliente},'{data_nota}','{numero_nota}','{valor_nota}');")

def alterar_nota():
    pass

def excluir_nota(num_nota):
    retorno = conect_bd(f'delete from nota where numero_nota = {num_nota}')

def adicionar_cliente():
    #insert into cliente(nome, endereco, bairro, cep, telefone, whatsapp, responsavel) values
    #('Maria Selma', 'Al. Jequitibas, 1579', 'Roseira', '07619-020', '(11) 9.1122.3344', '(11) 9.1122.3344', 'Selma');

    pass

def alterar_cliente():
    pass

def excluir_cliente(cod_cliente):
    retorno = conect_bd(f'delete from cliente where cod_cliente = {cod_cliente};'
                        f'delete from nota where cod_cliente = {cod_cliente};')

excluir_cliente(10)