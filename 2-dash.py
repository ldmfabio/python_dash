import dash
from dash import dcc, html
from datetime import datetime

app = dash.Dash()
app.layout = html.Div(
    children = [
        html.Img(src="https://github.com/ldmfabio.png"),
        html.Hr(),
        html.H1('Testando Dash com HTML'),
        html.Span(
            children= [
                f'Hoje é {datetime.now().strftime("%d/%m/%Y")}',
                html.Br(),
                'Desenvolvido por ', html.B('Fábio Longo de Moura-ldmfabio'),
                html.Br(),
                html.I('Professor do IFC-Campus Araquari')
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
