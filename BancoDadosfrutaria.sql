
create table enderecos(
	id_endereco serial primary key,
	rua varchar not null,
	numero int not null,
	bairro varchar not null,
	cidade varchar not null,
	uf varchar not null
	

);

create table clientes(

	id_cliente serial primary key,
	cpf_client varchar not null,
	nome_cli varchar not null,
	email_cli varchar,
	telefone_c varchar not null,
	dt_nasc date, 
	id_endereco int,
	foreign key(id_endereco)
	REFERENCES enderecos(id_endereco)
);


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


create table produtos(
	id_produto serial primary key,
	nome_produto varchar not null,
	quant_produto int,
	peso int,
	preco int not null
	
);




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




create table pedidos_has_produtos(
	id_pedido_has_produtos serial primary key,
	
	id_pedido int,
	foreign key(id_pedido)
	REFERENCES pedidos(id_pedido),
	
	id_produto int,
	foreign key(id_produto )
	REFERENCES produtos(id_produto )


);

insert into enderecos(rua,numero,bairro,cidade,uf) values ('Av. Getulio Vargas',50 , 'Centro', 'Diadema', 'SP');
insert into enderecos(rua,numero,bairro,cidade,uf) values ('Av. das Flores',60 , 'Urauna', 'Diadema', 'SC');
insert into enderecos(rua,numero,bairro,cidade,uf) values ('Rua das Palmeiras',100 , 'Centro', 'Joinville', 'SC');
    

insert into clientes(cpf_client,nome_cli,email_cli,telefone_c,dt_nasc,id_endereco ) values('1234567891234567','Jairo Santos', 'jairo@gmail.com','(47) 999999912','2000-08-09', 2);
insert into clientes(cpf_client,nome_cli,email_cli,telefone_c,dt_nasc,id_endereco ) values('1234245666565555','Bia Morais Santos', 'bia@gmail.com','(47) 994459912','1990-12-09', 1);
insert into clientes(cpf_client,nome_cli,email_cli,telefone_c,dt_nasc,id_endereco ) values('0987658657363523','Ana Maria Ribas', 'anam@gmail.com','(47) 988776655','2001-08-04', 3);


insert into funcionarios(cpf_funcionario, nome_func, dt_nasc_func, telefone_func, email_func, id_endereco)
values
    ('12345678901', 'João da Silva', '1990-07-12', '47 99998060', 'joao@gmail.com', 1),
    ('98765432109', 'Maria Souza', '2000-06-11', '47 99993455', 'maria@egmail.com', 2),
    ('55555555555', 'José Santos', '1990-08-05', '47 988776655', 'jose@gmail.com', 3);
  
   
   
  insert into fornecedores(cpf_cnpj,nome_empresa,telefone_for,email_for,id_endereco) 
    values ( '78.333.123/0004-90', 'Agrifrut LTDA', '47 88889999', 'agrifrut@gmail.com',1),
    ( '30.345.553/0008-91', 'Legum LTDA', '47 33445599', 'legum@gmail.com',2),
    ( '20.333.453/0009-08', 'Polpas LTDA', '47 45678999', 'polpas@gmail.com',3);
   
   insert into produtos(nome_produto,quant_produto,peso,preco)
    VALUES ('Tomate',50,7,3.99),
    		('Cebola',45,8,2.99),
    		('Limao',30,4,1.99),
  			('Colve',10,1,1.99),
  			('Banana',30,9,2.99),
  			('Maçã',30,9,5.99),
  			('Uva',30,4,8.99);
  			
  INSERT INTO pedidos(quant_pedido, dt_pedido, id_cliente, matricula)
    VALUES (3,'2023-08-09',1,2),
    		(8,'2023-03-16',3,1),
    		(15,'2023-03-09',2,3);
    	
INSERT INTO pedidos(quant_pedido, dt_pedido, id_cliente, matricula)
    VALUES (5,'2023-08-12',1,1);

INSERT INTO fornecedores_has_produtos(data, custo, id_fornecedor, id_produto)
    VALUES ('2023-07-07',1000,1,2),
    		('2023-07-12',2000,2,3),
    		('2023-07-09',500,3,2),
    		('2023-06-02',1500,2,1),
    		('2023-08-12',2000,3,1);
   
 INSERT INTO pedidos_has_produtos(id_pedido, id_produto)
    VALUES (1,2),
    		(1,3), 
    		(1,1), 
    		(2,2), 
    		(2,3),
    		(3,1), 
    		(3,2), 
    		(3,3); 
    		



