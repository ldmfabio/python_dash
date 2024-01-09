from dash import Dash, dcc, html, callback, Input, Output

app = Dash()

app.layout = html.Div([
    html.H4('Testando Callback no Dash'),
    html.Div([
        "Input",
        dcc.Input(id='my-input', value='teste', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output')
])

@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)

def update_output_div(input_value):
    return f'Output: {input_value}'

if __name__ == '__main__':
    app.run_server(debug=True)
