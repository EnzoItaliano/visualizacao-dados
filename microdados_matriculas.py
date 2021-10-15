import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv('data/Microdados_EOL_Matriculas_Ano_2019.csv', encoding = "ISO-8859-1", sep = ';', chunksize=50000)
y = 0

for x in tabela:
    # display(x)
    y = x
    break

# Dados faltando
y = y.drop("DESC_CICLO_ENSINO", axis=1)
y = y.drop("DESC_TIPO_PROGRAMA", axis=1)
y = y.drop("CD_PARECER_CONCL_FIN", axis=1)
y = y.drop("DESC_PARECER_CONCL_FIN", axis=1)

# Não consta no dicionário de variáveis
y = y.drop("DUR_DIA_HORA", axis=1)
y = y.drop("DUR_DIA_MIN", axis=1)
y = y.drop("X_SEMANA", axis=1)

y["DUR_DIA_TURMA"] = pd.to_numeric(y["DUR_DIA_TURMA"], errors="coerce")

y = y.dropna(how="any", axis=0)
# y.info()

from wordcloud import WordCloud
text = y['NOME_ESCOLA'].str.replace(',', '').str.replace(' ', '_').str.cat(sep=' ')
# print(text)
wordcloud = WordCloud(background_color="black",
                      width=1980, height=1080).generate(text)

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
 
plt.imshow(wordcloud)
wordcloud.to_file("summary_wordcloud.png")