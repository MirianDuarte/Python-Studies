n = int(input('Digite um numero: '))

d = n * 2 #drobo
t = n * 3 #triplo
r = n ** (1/2) #raiz quadrada

print('O dobro {} vale {}'.format(n, d))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}'. format(n, t, n, r))


# outra forma de fazer esse exercicio

n = int(input('Digite um numero: '))

print('O dobro de {} vale {}'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(n, (n*3), n, pow(n, (1/2))))