import array as arr
import string
import time, sys
from random import randint
import numpy as np


lista_clientes = []
#MenuPrincipal
def listaClientesCadastros(ident):
    for i in range(len(lista_clientes)):              
                if lista_clientes[i][0] == ident:
                    print(lista_clientes[i])
            
def menuPrincipal():
    print('[1] Cadastrar')
    print('[2] Acessar Usuário')
    print('[0] Sair')
    first_choice = int(input('Escolha a função desejada: '))
    while first_choice < 0  or first_choice > 3:
        print('Opção invalidade. Por Favor, selecione uma das opções do menu')
        first_choice = int(input('Escola a função desejada: '))
    else:
        if first_choice == 0:
            print('Saindo...')
            for i in range(0, 10):
                sys.stdout.write('\r{}'.format(i))
                sys.stdout.flush()
                time.sleep(1)
                exit()
    #Cadastrar
        elif first_choice == 1:
            cadastrar_de_novo = 's' 
            while cadastrar_de_novo == 's':
                print('Cadastro')
                nome = input('Nome: ')            
                telefone = input('Telefone: ')
                endereco = input('Endereço: ')         
                print('{}, {}, {}'.format(nome,telefone,endereco))
                ident = randint(0,999)
                lista_clientes.append((ident,nome,telefone,endereco))
                print('Usuário Cadastrado Com Sucesso, código: ', ident)
                cadastrar_de_novo = input('Deseja Cadastrar novo Usuário? [s/n]: ')
            first_choice = menuPrincipal()
#Acessar Usuário
        elif first_choice == 2:
            ident = int(input('Qual o código do usuario? '))
            listaClientesCadastros(ident)
            first_choice = menuPrincipal()
menuPrincipal()