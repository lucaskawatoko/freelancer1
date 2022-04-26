import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#arquivo helpers contem funções que ajustam os dados de cada turma e cada disciplina
from helpers import adicao_pontos, raiz_quadrada, equacao_normal, modifica_conceitos


#lendo planilha em formato xlsx

df = pd.read_excel(r"app\app\students.xlsx", sheet_name='Marks', engine='openpyxl')

#filtrando Turma A por Disciplina
turma_A_geo = df.loc[df['Class'] == 'A']['Geography'].sort_values(ascending=True)
turma_A_hist = df.loc[df['Class'] == 'A']['History'].sort_values(ascending=True)
turma_A_mat = df.loc[df['Class'] == 'A']['Maths'].sort_values(ascending=True)
turma_A_bio = df.loc[df['Class'] == 'A']['Biology'].sort_values(ascending=True)
turma_A_phy = df.loc[df['Class'] == 'A']['Physics'].sort_values(ascending=True)
turma_A_che = df.loc[df['Class'] == 'A']['Chemistry'].sort_values(ascending=True)
turma_A_lit = df.loc[df['Class'] == 'A']['Literature'].sort_values(ascending=True)

#filtrando Turma B por Disciplina
turma_B_geo = df.loc[df['Class'] == 'B']['Geography'].sort_values(ascending=True)
turma_B_hist = df.loc[df['Class'] == 'B']['History'].sort_values(ascending=True)
turma_B_mat = df.loc[df['Class'] == 'B']['Maths'].sort_values(ascending=True)
turma_B_bio = df.loc[df['Class'] == 'B']['Biology'].sort_values(ascending=True)
turma_B_phy = df.loc[df['Class'] == 'B']['Physics'].sort_values(ascending=True)
turma_B_che = df.loc[df['Class'] == 'B']['Chemistry'].sort_values(ascending=True)
turma_B_lit = df.loc[df['Class'] == 'B']['Literature'].sort_values(ascending=True)

#filtrando Turma C por Disciplina
turma_C_geo = df.loc[df['Class'] == 'C']['Geography'].sort_values(ascending=True)
turma_C_hist = df.loc[df['Class'] == 'C']['History'].sort_values(ascending=True)
turma_C_mat = df.loc[df['Class'] == 'C']['Maths'].sort_values(ascending=True)
turma_C_bio = df.loc[df['Class'] == 'C']['Biology'].sort_values(ascending=True)
turma_C_phy = df.loc[df['Class'] == 'C']['Physics'].sort_values(ascending=True)
turma_C_che = df.loc[df['Class'] == 'C']['Chemistry'].sort_values(ascending=True)
turma_C_lit = df.loc[df['Class'] == 'C']['Literature'].sort_values(ascending=True)

#gerando um gráfico dos dados originais
x1 = turma_C_mat.values
y1 = equacao_normal(x1)
media1 = np.mean(x1)

x2 = raiz_quadrada(x1)
y2 = equacao_normal(x2)
media2 = np.mean(x2)

x3 = adicao_pontos(x1)
y3 = equacao_normal(x3)
media3 = np.mean(x3)

bins=[0,60,70,80,90,100]

#transformação das notas em conceitos
df['History'] = df['History'].apply(lambda x: modifica_conceitos(x))
df['Geography'] = df['Geography'].apply(lambda x: modifica_conceitos(x))
df['Maths'] = df['Maths'].apply(lambda x: modifica_conceitos(x))
df['Biology'] = df['Biology'].apply(lambda x: modifica_conceitos(x))
df['Physics'] = df['Physics'].apply(lambda x: modifica_conceitos(x))
df['Chemistry'] = df['Chemistry'].apply(lambda x: modifica_conceitos(x))
df['Literature'] = df['Literature'].apply(lambda x: modifica_conceitos(x))

#Exibindo os dados após mudança de notas para conceito
print(df)

plt.style.use('seaborn')
fig, ax  = plt.subplots(1,4, figsize=(10,5))
ax[0].hist(x1, bins=[0,60,70,80,90,100], color='#3F5D7D', density=True, alpha=0.5)
ax[0].plot(x1, y1, color='#3F5D7D', linewidth=1)
ax[0].set_title('Histograma')

ax[1].plot(x1,y1, color='black',linestyle='dashed')
ax[1].scatter(x1, y1, marker='o', s=25, color='red')
ax[1].fill_between(x1,y1, color='blue', alpha=0.2)
ax[1].set_xlabel('Notas sem ajuste')
ax[1].set_ylabel('Dimensionamento Probabilidade')
ax[1].set_title('Notas não Normalizadas ')

ax[2].plot(x2,y2, color='black',linestyle='dashed')
ax[2].scatter(x2, y2, marker='o', s=25, color='red')
ax[2].fill_between(x2,y2, color='blue', alpha=0.2)
ax[2].set_xlabel('Notas ajustadas com raiz quadrada')
ax[2].set_ylabel('Dimensionamento Probabilidade após ajuste')
ax[2].set_title('Notas Normalizadas com Raiz quadrada ')

ax[3].plot(x3,y3, color='black',linestyle='dashed')
ax[3].scatter(x3, y3, marker='o', s=25, color='red')
ax[3].fill_between(x3,y3, color='blue', alpha=0.2)
ax[3].set_xlabel('Notas ajustadas com adição de pontos')
ax[3].set_ylabel('Dimensionamento Probabilidade após ajuste')
ax[3].set_title('Notas Normalizadas com Adição de pontos ')

fig.tight_layout()
plt.show()



