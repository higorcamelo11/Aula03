idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('\nVocê é maior de idade!')
else:
    print('\nVocê é menor de idade.')

#--------------------------------------------------------#

# Classificação por Pontos #
pontos = int(input('Informe os pontos: '))

if pontos >= 100:
    total = pontos + 10
    print(f'Excelente! Agora você têm {total} pontos')

elif pontos >= 50:
    total = pontos + 5
    print(f'Bom desempenho! Você tem {total} pontos')
else:
    print(f'Treine mais! Pontuação {pontos} pontos')

print('Fim.')