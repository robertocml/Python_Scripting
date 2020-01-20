import dash
import dash_core_components as dcc
import dash_html_components as html

#...Dash its actually a Flask app
app = dash.Dash()
app.layout = html.Div(children=[
    html.H1('Dash Basics'),
    dcc.Graph(id='test',
                figure={
                    'data' : [
                        {'x' : [1,2,3,4,5],'y' : [5,7,2,1,6], 'type' : 'line', 'name' : 'Perros'},
                        {'x' : [1,2,3,4,5],'y' : [5,7,2,1,6], 'type' : 'bar', 'name' : 'Gatos'},
                         ],
                    'layout' : {
                        'title' : 'Basic Dash tutorial                                                                                              v  '

                    }   
                })
    ])

    

if __name__ == '__main__':
    app.run_server(debug=True)
