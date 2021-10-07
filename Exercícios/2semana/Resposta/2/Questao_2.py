import pandas as pd

archive_uc = 'data_uc-modif.xlsx' # arquivo onde removi uma das tarifas sociais (teste)
archive_ts = 'data_ts.xlsx'

#um df para cada arquivo
dfuc = pd.read_excel(archive_uc)
dfts = pd.read_excel(archive_ts)

#transsforma uma coluna em uma lista para ser mais fácil encontrar
uc = dfuc['UC_TOT'].tolist()
cont = 0 #contador de UCs que não aparecem

for i in range(0,dfts.shape[0]):
    ts = dfts['UC'][i] #ts guarda o valor da UC da tarifa
    if not(ts in uc): #verifica se a UC da tarifa não está presente no banco de UC
        cont+=1
        print('-A UC',ts,'da Tarifia Social não se encontra no banco de UCs')#relatorio
if cont==0: # relatório também vai dizer se todas as UCs estão presentes
    print('Todas as UCs da Tarifia Social se encontram no banco de UCs')#relatorio
