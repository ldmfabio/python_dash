from dash import Dash, dcc, html

app = Dash()

app.layout = html.Div(
    children=[
        html.H1('Testando Dash com HTML'),
        html.H2('Text',
            style={
                'font-size': '50px',
                'color': 'blue'
            }
        ),
        html.Img(
            src='https://github.com/ldmfabio.png',
            style={
                'width:': '150px',
                'height:': '150px'
            }
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
