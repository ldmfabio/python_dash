from dash import Dash, dcc, html, dash_table
import pandas as pd

app = Dash()

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)
# print(df)

app.layout = html.Div([
    html.Div(children='DataTable com Dash'),
    dash_table.DataTable(
        data=df.to_dict('records'),
        page_size=10,
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
