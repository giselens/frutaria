import psycopg2


def execute(consulta_sql):
    db_params = {
        "host": "localhost",
        "database": "frutaria_online",
        "user": "postgres",
        "password": "postgres",
    }
    try:
        connection = psycopg2.connect(**db_params)

        cursor = connection.cursor()

        cursor.execute(consulta_sql)

        if (
            "insert" in consulta_sql
            or "update" in consulta_sql
            or "delete" in consulta_sql
        ):
            connection.commit()
            return
        resultados = cursor.fetchall()
        return resultados

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar-se ao banco de dados:", error)
        return None

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


consulta = """ select * from clientes; """


def listaclientes():
    selectconsulta = """ select id_cliente, nome_cli, cpf_client,
    email_cli, telefone_c, dt_nasc, id_endereco from clientes; """
    lista = execute(selectconsulta)

    for linha in lista:
        print(
            f"ID:{linha[0]} Nome: {linha[1]} CPF:{linha[2]} E-mail: {linha[3]} Telefone: {linha[4]} Nascido: {linha[5]} Endereço: {linha[6]}"
        )

    return lista


def cadastrarcliente(cpf, nome, email, telefone, nascimento, endereco):
    if endereco == None:
        endereco = "NULL"

    selectconsulta = f""" insert into clientes(cpf_client, nome_cli, 
    email_cli, telefone_c, dt_nasc, id_endereco)
    values ('{cpf}','{nome}','{email}','{telefone}','{nascimento}',{endereco});
    """
    execute(selectconsulta)

    feedback = "Dados inseridos com sucesso!"
    return feedback


def cadastrarendereco(rua, numero, bairro, cidade, estado):
    selectconsulta = f""" insert into enderecos(rua,numero,bairro,cidade,uf)
     values ('{rua}','{numero}','{bairro}','{cidade}','{estado}') """
    execute(selectconsulta)
    return None


def atualiza_todos_campos_do_cliente(
    id, cpf, nome, email, telefone, nascimento, endereco
):
    if endereco == None:
        endereco = "NULL"

    selectconsulta = f""" update clientes set cpf_client = '{cpf}', nome_cli = '{nome}', 
    email_cli = '{email}', telefone_c = '{telefone}', dt_nasc = '{nascimento}', id_endereco = {endereco}
    where id_cliente = {id};"""
    execute(selectconsulta)

    feedback = "Dados Atualizados!"
    return feedback


def deletar_cadastro_de_cliente(id):
    selectconsulta = f""" delete from clientes where  id_cliente = {id};"""
    execute(selectconsulta)

    feedback = "Cadastro apagado!"
    return feedback


def listar_produtos():
    selectconsulta = """ select  * from produtos; """
    lista = execute(selectconsulta)
    return lista


def cadastrar_produto(nome, quantidade, peso_p, preco_p):
    selectconsulta = f""" insert into produtos(nome_produto,quant_produto,peso,preco)
    VALUES ('{nome}',{quantidade},{peso_p},{preco_p});"""
    execute(selectconsulta)

    feedback = "Dados inseridos com sucesso!"
    return feedback


def atualiza_produto(codigo, nome, quantidade, peso_p, preco_p):
    selectconsulta = f""" update produtos set nome_produto = '{nome}', quant_produto = {quantidade},peso = {peso_p},preco = {preco_p}
    where id_produto = {codigo};"""
    execute(selectconsulta)

    feedback = "Dados Atualizados!"
    return feedback


def deleta_cadastro_produto(id):
    selectconsulta = f""" delete from produtos where  id_produto = {id};"""
    execute(selectconsulta)

    feedback = "Cadastro apagado!"
    return feedback


def listar_fornecedores():
    selectconsulta = """ select  * from fornecedores; """
    lista = execute(selectconsulta)
    return lista


def deletar_fornecedor(codigo):
    selectconsulta = f""" delete from fornecedores where  id_fornecedor = {codigo};"""
    execute(selectconsulta)

    feedback = "Cadastro apagado!"
    return feedback


def cadastro_de_fornecedor(nome, cpf_ou_cnpj, email, telefone, endereco):
    if endereco == None:
        endereco = "NULL"

    selectconsulta = f""" insert into fornecedores(cpf_cnpj,nome_empresa,telefone_for,email_for,id_endereco) 
    values ('{cpf_ou_cnpj}','{nome}','{telefone}','{email}',{endereco} );"""
    execute(selectconsulta)

    feedback = "Dados inseridos com sucesso!"
    return feedback


def atualizar_cadastro_de_fornecedor(
    id_f, nome, cpf_ou_cnpj, email, telefone, endereco
):
    if endereco == None:
        endereco = "NULL"

    selectconsulta = f""" update fornecedores set cpf_cnpj = '{cpf_ou_cnpj}',nome_empresa = '{nome}',telefone_for = '{telefone}',
    email_for = '{email}',id_endereco = {endereco} where id_fornecedor = {id_f};"""
    execute(selectconsulta)

    feedback = "Dados Atualizados!"
    return feedback


def menu():
    print("\n")
    print("--------- MENU --------------")
    print("\n")
    print("1. Listar todos os clientes")
    print("2. Cadastrar cliente")
    print("3. Atualizar dados do cliente")
    print("4. Apagar cadastro de cliente")
    print("\n")
    print("--------- Produtos --------------")
    print("\n")
    print("5. Lista de produtos")
    print("6. Cadastrar produto")
    print("7. Atualizar cadastro do produto")
    print("8. Apagar cadastro do produto")
    print("\n")
    print("--------- Forncedores--------------")
    print("\n")
    print("9. Listar todos os fornecedores")
    print("10. Cadastrar fornecedor")
    print("11. Atualizar dados do fornecedor")
    print("12. Apagar cadastro do fornecedor")
    print("\n")

    opcao = input("Escolha a opção desejada: ")

    return opcao


def tratamentodeopcoes(opcao):
    if opcao == "1":
        lc = listaclientes()
        return lc
    if opcao == "2":
        nome = input("Nome: ")

        cpf = input("Cpf: ")

        email = input("E-mail: ")

        telefone = input("Telefone: ")

        nascimento = input("Data de Nascimento: ")
        print("\n------Endereço------\n")
        rua = input("Rua:")
        numero = input("Numero:")
        bairro = input("Bairro:")
        cidade = input("Cidade:")
        estado = input("Estado:")

        ie = cadastrarendereco(rua, numero, bairro, cidade, estado)

        ic = cadastrarcliente(cpf, nome, email, telefone, nascimento, 4)
        return ic
    if opcao == "3":
        id = input("Digite o id do cliente que deseja atualizar os dados:")

        nome = input("Nome: ")

        cpf = input("Cpf: ")

        email = input("E-mail: ")

        telefone = input("Telefone: ")

        nascimento = input("Data de Nascimento: ")

        atds = atualiza_todos_campos_do_cliente(
            id, cpf, nome, email, telefone, nascimento, None
        )
        return atds
    if opcao == "4":
        print("Digite o id do cliente que deseja apagar o registro:")
        id = input()
        d = deletar_cadastro_de_cliente(id)
        return d

    if opcao == "5":
        lp = listar_produtos()
        return lp
    if opcao == "6":
        print("Dados cadatrais do produto:")
        nome = input("Nome: ")

        quantidade = input("Quantidade: ")
        peso = input("Peso kg:")
        preco = input("Preço R$: ")

        cp = cadastrar_produto(nome, quantidade, peso, preco)
        return cp
    if opcao == "7":
        codigo = input("Digite o código do produto que deseja atualizar: ")
        nome = input("Nome: ")

        quantidade = input("Quantidade: ")
        peso = input("Peso kg:")
        preco = input("Preço R$: ")

        atp = atualiza_produto(codigo, nome, quantidade, peso, preco)
        return atp
    if opcao == "8":
        codigo = input("Digite o código do produto que deseja apagar: ")
        dlp = deleta_cadastro_produto(codigo)
        return dlp
    if opcao == "9":
        lf = listar_fornecedores()
        return lf
    if opcao == "10":
        nome = input("Empresa: ")

        cpf_ou_cnpj = input("Cpf ou Cnpj: ")

        email = input("E-mail: ")

        telefone = input("Telefone: ")
        cf = cadastro_de_fornecedor(nome, cpf_ou_cnpj, email, telefone, None)
        return cf
    if opcao == "11":
        codigo = input("Digite o código do fornecedor que deseja atualizar cadastro: ")

        nome = input("Empresa: ")

        cpf_ou_cnpj = input("Cpf ou Cnpj: ")

        email = input("E-mail: ")

        telefone = input("Telefone: ")
        atf = atualizar_cadastro_de_fornecedor(
            codigo, nome, cpf_ou_cnpj, email, telefone, None
        )
        return atf

    if opcao == "12":
        codigo = input("Digite o código do cadastro que deseja apagar:")
        dlf = deletar_fornecedor(codigo)
        return dlf


escolha = menu()
tratamentodeopcoes(escolha)
