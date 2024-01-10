import numpy as np
import holoviews as hv
import panel as pn
hv.extension('bokeh')
points = [(0.1*i, np.sin(0.1*i)) for i in range(100)]
hv.Curve(points)
print("wave")

from bokeh.plotting import show
show(hv.render(hv))