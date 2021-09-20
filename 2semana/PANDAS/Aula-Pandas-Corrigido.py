import pandas as pd

archive = 'Dados_Bombas_Gasolina.xlsx'

df = pd.read_excel(archive)

row = df.shape[0]
# column = []
# for i in df.columns: column.append(i)

serie = list(range(1000,11000,1000))
maquina_def = []

for c in range(0,len(serie)-1):
    cont = 0
    for r in range(0, row):
        if serie[c] <= df['SERIAL'][r] < serie[c+1]:
            if str(df['VALOR_FIN'][r]) != 'nan':
                preco = float(df['PRECO_LITRO'][r])
                litros = float(df['LITRO'][r])
                valor = float(df['VALOR_FIN'][r])
                
                valor_calc = preco*litros
                
                # PONTO INCORRETO DO VÍDEO ORIGINAL, NÃO É COLOCADO O 2° PARAMETRO
                # DA FUNÇÃO ROUND QUE DELIMITA PARA QUANTAS CASAS DECIMAIS É FEITO
                # O ARREDONDAMENTO
                # valor_calcUP = float ('{:.2f}'.format(round(valor_calc+0.02)))
                # valor_calcDW = float ('{:.2f}'.format(round(valor_calc-0.02)))
                # PARA ESSE EXEMPLO, DEVE SER COLOCADO O 2 PARA DEFINIR 2 CASAS DE
                # ARREDONDAMENTO DO NOSSO FLOAT
                valor_calcUP = float ('{:.2f}'.format(round(valor_calc+0.02,2)))
                valor_calcDW = float ('{:.2f}'.format(round(valor_calc-0.02,2)))
                
                if not(valor_calcDW <= valor <= valor_calcUP):
                    print('\n- Máquina com defeito! Serial '+str(df['SERIAL'][r]))
                    cont += 1
            else:
                print('\n- Máquina com defeito! Serial '+str(df['SERIAL'][r]))
                cont += 1
    maquina_def.append(cont)

import numpy as np
y = np.array(maquina_def)
x = np.arange(1,10,1)

import matplotlib.pyplot as plt

plt.grid(True, axis = 'y', linestyle = 'dashed')
plt.title('Total de defietos em 9 dias')
plt.plot([1,9],[1,1], 'r--')#meta
plt.plot([1,9],[y.mean(), y.mean()],'g--')#média
plt.bar(x,y,color='b')

plt.legend(['Meta', 'Média de defeitos', 'Maquinas com defeito'])
plt.xticks(x)
plt.ylabel('Máquinas com Defeito')
plt.xlabel('Dias')

plt.show()






