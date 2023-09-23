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

#CRUD PARA TABELA CLIENTES

def lista_clientes():
    selectconsulta = """ select id_cliente, nome_cli, cpf_client,
    email_cli, telefone_c, dt_nasc, id_endereco from clientes; """
    lista = execute(selectconsulta)

    for linha in lista:
        print(
            f"ID:{linha[0]} Nome: {linha[1]} CPF:{linha[2]} E-mail: {linha[3]} Telefone: {linha[4]} Nascido: {linha[5]} Endereço: {linha[6]}"
        )

    return lista


def cadastrar_cliente(cpf, nome, email, telefone, nascimento, endereco):
    if endereco == None:
        endereco = "NULL"

    selectconsulta = f""" insert into clientes(cpf_client, nome_cli, 
    email_cli, telefone_c, dt_nasc, id_endereco)
    values ('{cpf}','{nome}','{email}','{telefone}','{nascimento}',{endereco});
    """
    execute(selectconsulta)

    feedback = "Dados inseridos com sucesso!"
    return feedback


def cadastrar_endereco(rua, numero1, bairro, cidade, estado):
    selectconsulta = f""" insert into enderecos(rua,numero,bairro,cidade,uf)
     values ('{rua}','{numero1}','{bairro}','{cidade}','{estado}') """
    execute(selectconsulta)

    return None


def atualizar_endereco(ide, numero1, bairro, cidade, estado):
    selectconsulta = f"""update enderecos set numero = {numero1}, 
    bairro ='{bairro}', cidade = '{cidade}', uf = '{estado}' 
    where id_endereco = {ide} """

    execute(selectconsulta)

    feedback = "Dados Atualizados!"
    return feedback


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


#CRUD PARA TABELA PRODUTOS

def listar_produtos():
    selectconsulta = """ select  * from produtos; """
    lista = execute(selectconsulta)

    for linha in lista:
        print(
            f"Id: {linha[0]} Nome: {linha[1]} Quantidade: {linha[2]} Peso: {linha[3]} Preço: {linha[4]}"
        )
    return None


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

#CRUD PARA TABELA FORNECEDORES

def listar_fornecedores():
    selectconsulta = """ select  * from fornecedores; """
    lista = execute(selectconsulta)
    for linha in lista:
        print(
            f"Id: {linha[0]} CNPJ/CPF: {linha[1]} Empresa: {linha[2]} Telefone: {linha[3]} E-mail: {linha[4]} IdEndereço: {linha[5]}"
        )
    return None


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

#CRUD PARA TABELA PEDIDOS

def listar_pedidos():
    selectconsulta = """SELECT * FROM pedidos;"""
    lista = execute(selectconsulta)
    for linha in lista:
        print(
            f"ID do Pedido: {linha[0]} Quantidade Pedido: {linha[1]} Data do Pedido: {linha[2]} ID do Cliente: {linha[3]} Matrícula do Funcionário: {linha[4]}"
        )
    return lista

def cadastrar_pedido(quantidade, dt_pedido, id_cliente, matricula):
    selectconsulta = f"""INSERT INTO pedidos(quant_pedido, dt_pedido, id_cliente, matricula)
    VALUES ({quantidade}, '{dt_pedido}', {id_cliente}, {matricula});"""
    execute(selectconsulta)

    feedback = "Pedido cadastrado com sucesso!"
    return feedback

def atualizar_pedido(id_pedido, quantidade, dt_pedido, id_cliente, matricula):
    selectconsulta = f"""UPDATE pedidos
    SET quant_pedido = {quantidade}, dt_pedido = '{dt_pedido}', id_cliente = {id_cliente}, matricula = {matricula}
    WHERE id_pedido = {id_pedido};"""
    execute(selectconsulta)

    feedback = "Pedido atualizado com sucesso!"
    return feedback

def deletar_pedido(id_pedido):
    selectconsulta = f"""DELETE FROM pedidos WHERE id_pedido = {id_pedido};"""
    execute(selectconsulta)

    feedback = "Pedido apagado com sucesso!"
    return feedback

#CRUD PARA TABELA FUNCIONARIOS

def listar_funcionarios():
    selectconsulta = """SELECT * FROM funcionarios;"""
    lista = execute(selectconsulta)
    for linha in lista:
        print(
            f"Matrícula: {linha[0]} CPF: {linha[1]} Nome: {linha[2]} Data de Nascimento: {linha[3]} Telefone: {linha[4]} E-mail: {linha[5]} ID do Endereço: {linha[6]}"
        )
    return lista

def cadastrar_funcionario(cpf, nome, dt_nasc, telefone, email, id_endereco):
    selectconsulta = f"""INSERT INTO funcionarios(cpf_funcionario, nome_func, dt_nasc_func, telefone_func, email_func, id_endereco)
    VALUES ('{cpf}', '{nome}', '{dt_nasc}', '{telefone}', '{email}', {id_endereco});"""
    execute(selectconsulta)

    feedback = "Funcionário cadastrado com sucesso!"
    return feedback

def atualizar_funcionario(matricula, cpf, nome, dt_nasc, telefone, email, id_endereco):
    selectconsulta = f"""UPDATE funcionarios
    SET cpf_funcionario = '{cpf}', nome_func = '{nome}', dt_nasc_func = '{dt_nasc}',
    telefone_func = '{telefone}', email_func = '{email}', id_endereco = {id_endereco}
    WHERE matricula = {matricula};"""
    execute(selectconsulta)

    feedback = "Funcionário atualizado com sucesso!"
    return feedback

def deletar_funcionario(matricula):
    selectconsulta = f"""DELETE FROM funcionarios WHERE matricula = {matricula};"""
    execute(selectconsulta)

    feedback = "Funcionário apagado com sucesso!"
    return feedback

#CRUD PARA TABELA FORNECEDORES_HAS_PRODUTOS

def listar_fornecedores_has_produtos():
    selectconsulta = """SELECT * FROM fornecedores_has_produtos;"""
    lista = execute(selectconsulta)
    for linha in lista:
        print(
            f"ID da relação: {linha[0]} Data: {linha[1]} Custo: {linha[2]} ID do Fornecedor: {linha[3]} ID do Produto: {linha[4]}"
        )
    return lista

def cadastrar_fornecedores_has_produtos(data, custo, id_fornecedor, id_produto):
    selectconsulta = f"""INSERT INTO fornecedores_has_produtos(data, custo, id_fornecedor, id_produto)
    VALUES ('{data}', {custo}, {id_fornecedor}, {id_produto});"""
    execute(selectconsulta)

    feedback = "Relação cadastrada com sucesso!"
    return feedback


def deletar_fornecedores_has_produtos(id_relacao):
    selectconsulta = f"""DELETE FROM fornecedores_has_produtos WHERE id_fornecedores_has_produtos = {id_relacao};"""
    execute(selectconsulta)

    feedback = "Relação apagada com sucesso!"
    return feedback

#CRUD DE PEDIDOS_HAS_PRODUTOS

def listar_pedidos_has_produtos():
    selectconsulta = """SELECT * FROM pedidos_has_produtos;"""
    lista = execute(selectconsulta)
    for linha in lista:
        print(
            f"ID da relação: {linha[0]} ID do Pedido: {linha[1]} ID do Produto: {linha[2]}"
        )
    return lista

def cadastrar_pedidos_has_produtos(id_pedido, id_produto):
    selectconsulta = f"""INSERT INTO pedidos_has_produtos(id_pedido, id_produto)
    VALUES ({id_pedido}, {id_produto});"""
    execute(selectconsulta)

    feedback = "Relação cadastrada com sucesso!"
    return feedback


def deletar_pedidos_has_produtos(id_relacao):
    selectconsulta = f"""DELETE FROM pedidos_has_produtos WHERE id_pedido_has_produtos = {id_relacao};"""
    execute(selectconsulta)

    feedback = "Relação apagada com sucesso!"
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
    print("--------- Fornecedores--------------")
    print("\n")
    print("9. Listar todos os fornecedores")
    print("10. Cadastrar fornecedor")
    print("11. Atualizar dados do fornecedor")
    print("12. Apagar cadastro do fornecedor")
    print("\n")
    print("--------- Pedidos --------------")
    print("\n")
    print("13 - Listar Pedidos")
    print("14 - Cadastrar Pedidos")
    print("15 - Atualizar Pedido")
    print("16 - Excluir Pedido")
    print("\n")
    print("--------- Funcionários --------------")
    print("\n")
    print("17 - Listar Funcionários")
    print("18 - Cadastrar Funcionários")
    print("19 - Atualizar Dados do Funcionário")
    print("20 - Excluir Funcionário (Desligado)")
    print("0. Sair")
    print("\n")

    opcao = input("Escolha a opção desejada: ")

    return opcao


def tratamentodeopcoes(opcao):
    if opcao == "1":
        lc = lista_clientes()
        return lc
    if opcao == "2":
        nome = input("Nome: ")

        cpf = input("Cpf: ")

        email = input("E-mail: ")

        telefone = input("Telefone: ")

        nascimento = input("Data de Nascimento: ")
        print("\n------Endereço------\n")
        rua = input("Rua:")
        numero1 = input("Numero:")
        bairro = input("Bairro:")
        cidade = input("Cidade:")
        estado = input("Estado:")

        cadastrar_endereco(rua, numero1, bairro, cidade, estado)
        consultaid = (
            f"""select id_endereco from enderecos e where e.numero = '{numero1}'  """
        )
        ide = execute(consultaid)

        ic = cadastrar_cliente(cpf, nome, email, telefone, nascimento, ide[0][0])
        return ic

    if opcao == "3":
        id = input("Digite o id do cliente que deseja atualizar os dados:")

        nome = input("Nome: ")

        cpf = input("Cpf: ")

        email = input("E-mail: ")

        telefone = input("Telefone: ")

        nascimento = input("Data de Nascimento: ")
        print("\n------Endereço------\n")

        rua = input("Rua:")
        numero1 = input("Numero:")
        bairro = input("Bairro:")
        cidade = input("Cidade:")
        estado = input("Estado:")

        consultaid = f""" select id_endereco from clientes where id_cliente = '{id}' """
        ide = execute(consultaid)
        atualizar_endereco(ide[0][0], numero1, bairro, cidade, estado)

        atds = atualiza_todos_campos_do_cliente(
            id, cpf, nome, email, telefone, nascimento, ide[0][0]
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
        print("\n------Endereço------\n")
        rua = input("Rua:")
        numero1 = input("Numero:")
        bairro = input("Bairro:")
        cidade = input("Cidade:")
        estado = input("Estado:")

        cadastrar_endereco(rua, numero1, bairro, cidade, estado)
        consultaid = (
            f""" select id_endereco from enderecos where numero ='{numero1}' """
        )
        ide = execute(consultaid)
        cf = cadastro_de_fornecedor(nome, cpf_ou_cnpj, email, telefone, ide[0][0])
        return cf

    if opcao == "11":
        codigo = input("Digite o código do fornecedor que deseja atualizar cadastro: ")

        nome = input("Empresa: ")

        cpf_ou_cnpj = input("Cpf ou Cnpj: ")

        email = input("E-mail: ")

        telefone = input("Telefone: ")
        print("\n------Endereço------\n")

        rua = input("Rua:")
        numero1 = input("Numero:")
        bairro = input("Bairro:")
        cidade = input("Cidade:")
        estado = input("Estado:")

        consultaid = f""" select id_endereco from fornecedores where id_fornecedor = '{codigo}' """
        ide = execute(consultaid)
        atualizar_endereco(ide[0][0], numero1, bairro, cidade, estado)

        atf = atualizar_cadastro_de_fornecedor(
            codigo, nome, cpf_ou_cnpj, email, telefone, ide[0][0]
        )
        return atf

    if opcao == "12":
        codigo = input("Digite o código do cadastro que deseja apagar:")
        dlf = deletar_fornecedor(codigo)
        return dlf
    
    if opcao == "13":
        lpd = listar_pedidos()
        return lpd
    if opcao == "14":
        id_pedido = input("Número do Pedido: ")
        quant_pedido = input("Quantidade do Pedido: ")
        dt_pedido = input("Data do Pedido: ")
        print("\n------Endereço Para Receber Pedido------\n")
        rua = input("Rua:")
        numero1 = input("Numero:")
        bairro = input("Bairro:")
        cidade = input("Cidade:")
        estado = input("Estado:")

        cadastrar_endereco(rua, numero1, bairro, cidade, estado)
        consultaid = (
            f""" select id_endereco from enderecos where numero ='{numero1}' """
        )
        ide = execute(consultaid)
        cpd = cadastrar_pedido(id_pedido, quant_pedido, dt_pedido, ide[0][0])
        return cpd
    
    if opcao == "15":
        id = input("Digite o id do pedido que deseja atualizar os dados:")
        quant_pedido = input("Quantidade do Pedido: ")
        dt_pedido = input("Data do Pedido: ")
        print("\n------Endereço------\n")
        rua = input("Rua:")
        numero1 = input("Numero:")
        bairro = input("Bairro:")
        cidade = input("Cidade:")
        estado = input("Estado:")
        consultaid = f""" select id_endereco from pedidos where id_pedido = '{codigo}' """
        ide = execute(consultaid)
        atualizar_endereco(ide[0][0], numero1, bairro, cidade, estado)
        atf = atualizar_pedido(
            id_pedido, quant_pedido, dt_pedido, ide[0][0]
        )
        return atf

    if opcao == "16":
        codigo = input("Digite o código do cadastro que deseja apagar:")
        dlp = deletar_pedido(codigo)
        return dlp

    if opcao == "17":
        lfunc = listar_funcionarios()
        return lfunc
    if opcao == "18":
        matricula = input("Matricula: ")
        cpf_funcionario = input("Cpf do Funcionario: ")
        nome_func = input("Nome do Funcionario: ")
        dt_nasc_func = input("Data de Nascimento: ")
        telefone_func= input("Telefone ")
        email_func = input("E-mail: ")
        print("\n------Endereço Funcionario------\n")
        rua = input("Rua:")
        numero1 = input("Numero:")
        bairro = input("Bairro:")
        cidade = input("Cidade:")
        estado = input("Estado:")

        cadastrar_endereco(rua, numero1, bairro, cidade, estado)
        consultaid = (
            f""" select id_endereco from funcionarios where numero ='{numero1}' """
        )
        ide = execute(consultaid)
        cf = cadastro_de_fornecedor(nome, cpf_ou_cnpj, email, telefone, ide[0][0])
        return cf

    if opcao == "19":
        codigo = input("Digite o código do funcionario que deseja atualizar cadastro: ")
        matricula = input("Matricula: ")
        cpf_funcionario = input("Cpf do Funcionario: ")
        nome_func = input("Nome do Funcionario: ")
        dt_nasc_func = input("Data de Nascimento: ")
        telefone_func= input("Telefone ")
        email_func = input("E-mail: ")
        print("\n------Endereço Funcionario------\n")

        rua = input("Rua: ")
        numero1 = input("Numero: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")

        consultaid = f""" select id_endereco from funcionarios where id_funcionario = '{codigo}' """
        ide = execute(consultaid)
        atualizar_endereco(ide[0][0], numero1, bairro, cidade, estado)

        atfunc = atualizar_funcionario(
            codigo, matricula, cpf_funcionario, nome_func, dt_nasc_func, telefone_func, email_func, ide[0][0]
        )
        return atfunc

    if opcao == "20":
        codigo = input("Digite o código do cadastro do funcionário que deseja apagar:")
        dlfunc = deletar_funcionario(codigo)
        return dlfunc
    

opcao = menu()
tratamentodeopcoes(opcao)
