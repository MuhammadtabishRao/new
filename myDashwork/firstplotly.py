import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(12)
x_values = np.random.randint(1,100,100)
y_values = np.random.randint(1,100,100)

data = [go.Scatter(x=x_values,y=y_values,
                    mode="markers",
                    marker = dict(size="petal_length" ,color="species",
                    symbol="pentagon" ,hover_data=['petal_width'] )
                    )]
                    
                    
                    
                    
                    
layout = go.Layout(title="Scatter plot",
                    xaxis = {"title":"X-axis"},
                    yaxis = dict(
                        title="Y-axis"),
                        hovermode = "closest"
                        
                    )
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename="scatter.html")
