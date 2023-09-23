create table clientes(

	id_cliente serial primary key,
	cpf_client varchar not null,
	nome_cli varchar not null,
	email_cli varchar,
	telefone_c varchar not null,
	dt_nasc varchar, 
	id_endereco int,
	foreign key(id_endereco)
	REFERENCES enderecos(id_endereco)
);


create table enderecos(
	id_endereco serial primary key,
	rua varchar not null,
	numero int not null,
	bairro varchar not null,
	cidade varchar not null,
	uf varchar not null
	

);

select * from clientes;

create table funcionarios(
	matricula serial primary key,
	cpf_funcionario varchar not null,
	nome_func  varchar not null,
	dt_nasc_func date,
	telefone_func  varchar,
	email_func  varchar,
	
	
	id_endereco int,
	foreign key(id_endereco)
	REFERENCES enderecos(id_endereco)
	
);

select * from funcionarios;


create table fornecedores(
	id_fornecedor serial primary key,
	cpf_cnpj varchar not null,
	nome_empresa varchar not null,
	telefone_for varchar not null,
	email_for varchar,
	
	id_endereco int,
	foreign key(id_endereco)
	REFERENCES enderecos(id_endereco)


);

select * from fornecedores;



create table produtos(
	id_produto serial primary key,
	nome_produto varchar not null,
	quant_produto int,
	peso int,
	preco int not null
	
);

select * from produtos;


create table pedidos(
	id_pedido serial primary key,
	quant_pedido int,
	dt_pedido date not null,
	
	id_cliente int,
	foreign key(id_cliente)
	REFERENCES clientes(id_cliente),
	
	matricula int,
	foreign key(matricula)
	REFERENCES funcionarios(matricula)

);

select * from pedidos;



create table fornecedores_has_produtos(
	id_fornecedores_has_produtos serial primary key,
	data date not null,
	custo int not null,
	
	id_fornecedor int,
	foreign key(id_fornecedor)
	REFERENCES fornecedores(id_fornecedor),
	
	id_produto int,
	foreign key(id_produto)
	REFERENCES produtos(id_produto)

);

select * from fornecedores_has_produtos ;


create table pedidos_has_produtos(
	id_pedido_has_produtos serial primary key,
	
	id_pedido int,
	foreign key(id_pedido)
	REFERENCES pedidos(id_pedido),
	
	id_produto int,
	foreign key(id_produto )
	REFERENCES produtos(id_produto )


);

select * from pedidos_has_produtos 



