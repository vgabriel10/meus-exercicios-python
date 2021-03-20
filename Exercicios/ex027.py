n = str(input('Digite o seu nome completo')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo Nome é {}'.format(nome[len(nome)-1])) #ele vai ler o último nome, porém o comando len começa
                                                        #contando do 1, já o split começa do zero, sendo assim
                                                        #tem que acrescentar o -1
                                                        #para ler o comando len sem ser na forma númerica tem
                                                        #que adicionar a variavel na frente como nesse exemplo




