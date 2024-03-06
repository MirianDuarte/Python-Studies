#aluguel por dia = R$60
# KM rodado = R$0,15

dias = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos Km você rodou com o carro? '))

pago = (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(pago))