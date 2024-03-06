preço = float(input('Qual é o preço do produto? R$')) #preço = 100% || novo = - 5%

novo = preço - (preço * 5 / 100)  #preço menos 5% do preço

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))