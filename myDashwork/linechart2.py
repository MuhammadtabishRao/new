import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(2)
data = np.linspace(0,1,100)


trace = go.Line(data,x="x_val",y="y_val", title="line chart")




pyo.plot(trace,filename="linechart2.html")