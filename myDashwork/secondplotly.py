import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(12)
x_values0 = np.random.randint(1,100,100)
y_values0 = np.random.randint(1,100,100)
x_values1 = np.random.randint(1,100,100)
y_values1 = np.random.randint(1,100,100)


data1 = go.Scatter(x=x_values0,
                    y=y_values0,
                    mode="markers",
                    marker=dict(
                        size=12,
                        name='sin',
                        color = "rgb(99,44,22)",
                        line= {"width":2}



                    ))
        



data2 = go.Scatter(x=x_values1+5,
                    y=y_values1+2,
                    mode='lines',
                        name='cos',
                        color = "rgb(56,200,77)",
                        



                    )
        

layout = go.Layout(title="hello plotly",
                    xaxis={"title":"my_X_axis"},
                    yaxis=dict(
                        title="my_Y_axis") ,
                        hovermode="closest"
                    )

data=[data1,data2]                  
fig=go.Figure(data=data, layout=layout)


pyo.plot(fig,filename="scatter2.html")
