# ## Questão 3

# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

# Lendo o arquivo JSON com os dados de faturamento
with open('faturamento.json', 'r') as file:
    data = json.load(file)

# Inicializando as variáveis de mínimo e máximo com o primeiro valor do vetor
min_faturamento = max_faturamento = data[0]
total_faturamento = 0
dias_com_faturamento_superior_media = 0

# Percorrendo o vetor de faturamento para encontrar o menor e o maior valor
for faturamento in data:
    if faturamento < min_faturamento:
        min_faturamento = faturamento
    elif faturamento > max_faturamento:
        max_faturamento = faturamento

    # Somando o valor do faturamento para calcular a média mensal
    total_faturamento += faturamento

# Calculando a média mensal
media_mensal = total_faturamento / len(data)

# Contando quantos dias tiveram faturamento superior à média mensal
for faturamento in data:
    if faturamento > media_mensal:
        dias_com_faturamento_superior_media += 1

# Imprimindo os resultados
print('Menor valor de faturamento diário:', min_faturamento)
print('Maior valor de faturamento diário:', max_faturamento)
print('Dias com faturamento superior à média mensal:', dias_com_faturamento_superior_media)