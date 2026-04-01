import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Criando a tabela de usuários
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER
)
""")

def cadastrar():
    print("\n--- Novo Cadastro ---")
    nome = input("Nome: ")
    try:
        idade = int(input("Idade: "))
        cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
        conn.commit()
        print("✅ Usuário cadastrado com sucesso!")
    except ValueError:
        print("❌ Erro: Digite um número válido para a idade.")

def listar():
    print("\n--- Lista de Usuários ---")
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    if not usuarios:
        print("Nenhum usuário encontrado.")
    for usuario in usuarios:
        print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Idade: {usuario[2]}")

def deletar():
    listar()
    try:
        id_usuario = int(input("\nDigite o ID do usuário para deletar: "))
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
        conn.commit()
        print("🗑️ Usuário removido!")
    except ValueError:
        print("❌ Erro: Digite um ID numérico válido.")

# Loop Principal
while True:
    print("\n======================")
    print("  SISTEMA DE CADASTRO ")
    print("======================")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Deletar")
    print("4 - Sair")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        deletar()
    elif opcao == "4":
        print("Encerrando... Até mais!")
        break
    else:
        print("Opção inválida!")
