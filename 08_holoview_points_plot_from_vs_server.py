# https://stackoverflow.com/questions/57971107/how-do-i-get-my-interactive-holoviews-graph-to-display-in-visual-studio-without
# library imports
import numpy as np
import pandas as pd
import holoviews as hv
hv.extension('bokeh', logo=False)
import panel as pn

# create sample data
data = np.random.normal(size=[50, 2])
df = pd.DataFrame(data, columns=['col1', 'col2'])

# create holoviews graph
hv_plot = hv.Points(df)

# display graph in browser
# a bokeh server is automatically started
bokeh_server = pn.Row(hv_plot).show(port=12345)

# stop the bokeh server (when needed)
bokeh_server.stop()
