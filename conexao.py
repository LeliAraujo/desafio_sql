import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()
#cursor.execute('CREATE TABLE alunos(id Int, nome VARCHAR (100), idade Int, curso VARCHAR (100))')
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(1, "Maria", 20, "Medicina")')
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(2, "João", 25, "Direito")')
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(3, "Ruben", 18, "Engenharia")')
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(4, "Guilherme", 21, "Administração")')
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(5, "Grazielle", 26, "Nutrição")')
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(6, "Michel", 28, "Economia")')
#dados = cursor.execute('SELECT * FROM alunos')
#dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade >20')
#dados = cursor.execute('SELECT nome FROM alunos WHERE curso = "Engenharia" ORDER BY nome asc')
#dados = cursor.execute('SELECT COUNT (*) FROM alunos')
#cursor.execute('UPDATE alunos SET idade = 19 WHERE idade = 26')
conexao.commit()
#cursor.execute('DELETE FROM alunos WHERE id = 1')

#cursor.execute('CREATE TABLE clientes(id INTERGER PRIMARY KEY, nome VARCHAR (100), idade INTERGER, saldo FLOAT)')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) Values(1, "Fernanda Maria", 32, 1000.00)')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) Values(2, "Maria José", 40, 1300.00)')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) Values(3, "Simone Ferreira", 48, 2000.00)')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) Values(4, "Jeannete Noronha", 46, 900.00)')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) Values(5, "Francisco Carlos", 52, 2200.00)')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) Values(6, "Claudio Peres", 51, 850.00)')

#dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade >30')

#dados = cursor.execute("SELECT AVG(saldo) FROM clientes").fetchone()[0]
#print(dados)

#dados = cursor.execute('SELECT * FROM clientes WHERE saldo=(SELECT MAX(saldo)FROM clientes)')

#dados = cursor.execute('SELECT Count(*) FROM clientes WHERE saldo >1000')
#for clientes in dados:
    #print (clientes)

#cursor.execute('UPDATE clientes SET saldo = 950 WHERE saldo = 850')

#cursor.execute('UPDATE clientes SET saldo = 980 WHERE saldo = 900')

#cursor.execute('DELETE FROM clientes WHERE id=5')
#cursor.execute('CREATE TABLE compras (id INTEGER PRIMARY KEY, cliente_id INTEGER, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) Values(1, 3, "camiseta", 40.00)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) Values(2, 2, "vestido", 70.00)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) Values(3, 4, "sapato", 85.00)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) Values(4, 1, "calça", 60.00)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) Values(5, 5, "saia", 35.00)')

#dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes JOIN compras ON clientes.id = compras.cliente_id')
#for usuario in dados:
    #print(usuario)

'''
    #for alunos in dados:
#print(alunos)    
conexao.commit()
conexao.close()