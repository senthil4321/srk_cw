import chipwhisperer as cw
import time

# https://courses.ideate.cmu.edu/16-223/f2021/text/code/pico-signals.html

print("Starting the Program")
try:
    scope = cw.scope()
except NameError:
    print("INFO: Unable to initialize USB connection. ?")

try:
    target = cw.target(scope)
except IOError:
    print("INFO: Caught exception on reconnecting to target - attempting to reconnect to scope first.")
    print("INFO: This is a work-around when USB has died without Python knowing. Ignore errors above this line.")
    target = cw.target(scope)

print("INFO: Found ChipWhisperer😍")
time.sleep(0.05)
scope.default_setup()
scope.adc.samples = 5000


print(target.baud)

ktp = cw.ktp.Basic()
key, pt = ktp.new_pair()
print(key)
print(pt)

target.simpleserial_write('p', pt)
ct = target.simpleserial_read('r', 16)
print(ct)

wave = cw.capture_trace(scope, target, pt).wave

values = []  # Array to collect values
for value in wave:
    # Perform operations on each value
    print(value)

    # value_str = "{:.3f}".format(value + 1)  # Convert to string with only 3 decimal places
    # print(value_str)
    values.append(value + 1)  # Collect value in array
import holoviews as hv
hv.extension('bokeh')
curve = hv.Curve(values).opts(fontscale=2, width=2000, height=1000, title='Analysis of Power Trace')

import panel as pn
bokeh_server = pn.Row(curve).show(port=12345)
bokeh_server.stop()

