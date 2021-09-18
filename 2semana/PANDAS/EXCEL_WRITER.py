# -*- coding: utf-8 -*-
"""
@author: mirla

LASI - UFPI
"""

import pandas as pd
import random
import numpy as np

def float_to_str (f):
    valor_str = ('{:.4f}'.format(round(f,4)))
    return valor_str

serial_num, preco_p_litro, litr, valor = [],[],[],[]
random.seed(1)
for i in range(0,30):
    ser = random.randint(1111, 9999)
    pre = random.uniform(5.99, 7.49)
    lit = random.uniform(2.00, 5.00)
    if i > (random.randint(15,32)):
        valor.append(np.NaN)
    else:
        val = pre*lit*(random.randint(1,2))
        valor_str = ('{:.2f}'.format(round(val,2)))
        valor.append(valor_str)
    serial_num.append(ser)
    preco_p_litro.append(float_to_str(pre))
    litr.append(float_to_str(lit))

dataf = {'SERIAL':serial_num,'PRECO_LITRO':preco_p_litro,'LITRO':litr,'VALOR_FIN':valor}    

df = pd.DataFrame(dataf)
archive = 'Dados_Bombas_Gasolina.xlsx'
w = pd.ExcelWriter('Dados_Bombas_Gasolina.xlsx', engine='xlsxwriter')
df.to_excel(w, sheet_name='Amostra', index=False)
w.save()
