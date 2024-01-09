import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

app = Dash()

# 1 - Criando nosso Dataframe
df = pd.DataFrame({
    'Fruits': ['Maçã', 'Laranja', 'Melão', 'Laranja', 'Uva', 'Melão'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['Gramado', 'São Luís', 'Gramado', 'Gramado', 'Curitiba', 'Curitiba']
})

# print(df)

# 2 - Criando nosso Gráfico
fig = px.bar(
    data_frame=df,
    x='Fruits',
    y='Amount',
    color='City',
    barmode='group'
)

fig.show()
