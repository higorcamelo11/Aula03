valor = float(input('\nValor da compra: '))

if valor > 250:
    desc = valor * 0.16
    total = valor - desc
    print(f'\nTotal com Desconto: {total}')
else:
    print(f'\nTotal: {valor}')
