kwh = float(input('Quantos kwh foram consumidos?'))
tipo = input('Qual o tipo de instalação (R, C ou I)')

if (tipo == 'R'):
	if kwh <= 500:
		preco = 0.4
	else:
		preco = 0.65

elif (tipo == 'C'):
	if kwh <= 1000:
		preco = 0.55
	else:
		preco = 0.6

elif (tipo == 'I'):
	if kwh <= 5000:
		preco = 0.55
	else:
		preco = 0.6
else:
	print('Instalação Inválida!')

print('Total a pagar: {}'.format(kwh * preco))