def menu():
    print('Bem vindo a Livraria do João Vitor')
    print('----------------------------------')
    print('--------- MENU  PRINCIPAL --------')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livros')
    print('3 - Remover Livro')
    print('4 - Sair')

def cadastrar_livro(id):
    print('----------------------------------')
    print('------ MENU CADASTRAR LIVRO ------')
   
    

#PROGRAMA PRINCIPAL

lista_livros = []
id_global = 5836107

while True:
    menu()
    op = int(input('>> '))

    if op == 1:
        cadastrar_livro(id)
    elif op == 2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        print('Encerrando programa . . . ')
        break