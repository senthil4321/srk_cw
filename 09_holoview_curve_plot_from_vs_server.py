import numpy as np
import holoviews as hv
hv.extension('bokeh')
points = [(0.1*i, np.sin(0.1*i)) for i in range(100)]
curve = hv.Curve(points)
print("wave")

import panel as pn
# a bokeh server is automatically started
bokeh_server = pn.Row(curve).show(port=12345)

# stop the bokeh server (when needed)
bokeh_server.stop()

