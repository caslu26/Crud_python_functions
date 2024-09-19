import sqlite3


def create_schema():
    # Criando o banco de dados
    conexao = sqlite3.connect('banco_dados')
    # Apontando para o banco de dados
    cursor = conexao.cursor()
    # Criando tabela no banco de dados (Descomente a linha abaixo na primeira execução)
    cursor.execute('CREATE TABLE IF NOT EXISTS Minha_Tabela(Data text, Nome text, Idade real)')
    conexao.commit()
    conexao.close()

def insert_into():
    # Solicitando dados do usuário
    data = input("Digite a data (formato: dd/mm/yyyy): ")
    nome = input("Digite o nome: ")
    idade = float(input("Digite a idade: "))

    # Inserindo os dados no banco
    conexao = sqlite3.connect('banco_dados')
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO Minha_Tabela VALUES (?, ?, ?)', (data, nome, idade))
    conexao.commit()
    conexao.close()

# Função para exibir dados do banco
def select_table():
    conexao = sqlite3.connect('banco_dados')
    cursor = conexao.cursor()  # Cria um novo cursor para a nova conexão
    consulta = cursor.execute('SELECT * FROM Minha_Tabela').fetchall()
    for linha in consulta:
        print(linha)
    conexao.close()  # Fechando a conexão ao final

#função para atualiza um dado no banco

def update_record():
    conexao = sqlite3.connect('banco_dados')
    cursor = conexao.cursor()
    # Atualizando o registro onde o nome é "Santiago"
    cursor.execute('UPDATE Minha_Tabela SET Idade = 29 WHERE Nome = "Santiago"')
    conexao.commit()  # Confirma a alteração
    conexao.close()  # Fecha a conexão

def delete_data():
    nome = input("Digite o nome: ")
    
    conexao = sqlite3.connect('banco_dados')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM Minha_Tabela VALUES (?)',(nome))
    conexao.commit()  # Confirma a alteração
    conexao.close()  # Fecha a conexão