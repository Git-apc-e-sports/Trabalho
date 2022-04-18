#Grafico CS






import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np




a= []
df=pd.read_excel(r'Data base definitivo.xlsx')
df.dropna(inplace=True)
df_array = df.values
lista_array = df_array.tolist()


#print(type(lista_array[0]))
##print(df.shape)



ganhos_cs = []
data = []
contador = 0
n = 1
datas = []
raw = [lista_array[i:i+n] for i in range(0, len(lista_array), n)]
for i in range(len(raw)):
    datas = raw.pop()
    print(datas)
#ganhos_cs = colunas [20]
#print (datas)
#print (ganhos_cs)    
    



#print(data)
contador = 0
for celula in df:
    contador += 1
    if contador == 21:
        ganhos_cs.append(celula)
ganhos_cs = df["ganhos_cs"].tolist()
data = df["data"].tolist()






fig = go.Figure()





fig.update_yaxes(title = 'Prêmios', title_font_color = 'black',
                 title_font_family = "Overpass",
title_font_size = 20, showgrid= True)



fig.update_xaxes(title = 'Ano', title_font_color = 'black',
                 title_font_family = "Overpass",
title_font_size = 20, showgrid=False)



fig.update_layout(title = 'Prêmios de campeonatos de CS:GO', title_pad_r=10000,
                  plot_bgcolor= '#edbb05' ,
 paper_bgcolor='#bd9c24', title_xanchor= 'left',
 title_yanchor= 'top', title_xref= 'paper', title_yref= 'paper', title_x= 0.23,
 title_font_family = "Gravitas One", title_font_size = 30,
 font=dict(color='black'))



fig.update_layout(showlegend= True)




fig.add_trace(go.Scatter(x=anos_px, y=premio_total, name =  '',
                         line = dict(color='black', width=3,
)))
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=anos_px,
        y=premio_total,
        marker=dict(
            color='white',
            size=10,

        ),

        showlegend=False

    )
)


#fig.show()