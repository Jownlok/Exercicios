def menu ():
    print('Bem vindo a Copiadora do João Vitor')
    print()
    print('Entre com o tipo de serviço desejado')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')

def menu2():
    print('Deseja adicionar algum serviço?')
    print('1 - Encadernação Simples - R$ 15,00')
    print('2 - Encadernação Capa Dura - R$ 40,00')
    print('0 - Não desejo mais nada')

def escolha_servico(servico):
    while servico not in ['dig', 'ico', 'ipb', 'fot']:
        print('Escolha inválida, entre com o tipo do serviço novamente')
        servico = input('>> ').lower()
    return servico

def num_pagina():
    while True:
        try:
            numerop = int(input('Entre com o número de páginas: '))
            if numerop > 20000:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com o número de páginas novamente.')
                print()
                continue
        
            return numerop
        
        except ValueError:
            print('Digite um número inteiro válido.')
            print()

def servico_extra():
    while True:
         
        op = int(input('>> '))
        if op == 1:
            total = (servico * n_paginas) + 15
            return total
            break

        if op == 2:
            total = (servico * n_paginas) + 40
            return total
            break

        if op == 0:
            total = (servico * n_paginas)
            return total
            break
    

#Programa Principal
total = 0
while True:
    menu()
    servico = input('>> ').lower()
    servico = escolha_servico(servico)
    if servico == 'dig':
        servico = 0.1
    elif servico == 'ipb':
        servico = 1
    elif servico == 'ico':
        servico = 0.4
    n_paginas = num_pagina()
    menu2()
    op = servico_extra(servico, n_paginas)
    print(total)