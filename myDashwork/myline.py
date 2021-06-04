import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(2)
x_val = np.linspace(0,1,100)
y_val = np.random.randn(100)

trace = go.Scatter(x=x_val,y=y_val, mode="markers", name="markers")
trace0 = go.Scatter(x=x_val,y=y_val+5, mode="line", name="line")


data=[trace,trace0]

layout = go.Layout(title="line chart",
                    xaxis = {"title":"X-axis"},
                    yaxis = dict(
                        title="Y-axis"),
                        hovermode = "closest"
                        
                    )
fig=go.Figure(data=data, layout=layout)
pyo.plot(fig,filename="linechart.html")