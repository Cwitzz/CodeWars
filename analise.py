import matplotlib.pyplot as plt

# valores fictícios de vendas dos produtos
vendas_produto_1 = [100, 200, 150, 300, 250, 350, 200, 300, 150, 400]
vendas_produto_2 = [110, 210, 140, 320, 240, 370, 220, 310, 160, 420]

plt.scatter(vendas_produto_1, vendas_produto_2)
plt.title('Relação entre as vendas dos produtos 1 e 2')
plt.xlabel('Vendas do Produto 1')
plt.ylabel('Vendas do Produto 2')
plt.show()
