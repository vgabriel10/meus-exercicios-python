"""
 Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
print('-'*40)
print(f'{"Tabela de Preços":^40}')
print('-'*40)
produtos = ('Lapis',1.00,
            'Borracha',2.00,
            'Mochila',40.00,
            'Caneta',1.99,
            'Caderno',15.99)

for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end='') # Próxima vez que rodar vai ser na mesma linha
    else:
        print(f'R$ {produtos[pos]:>5.2f}') # Quando entrar aqui nesse laço ele pula uma linha
print('-'*40)