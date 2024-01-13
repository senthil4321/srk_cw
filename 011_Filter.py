import Smoothing
import MedianFilter
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
scope.adc.samples = 500


print(target.baud)

ktp = cw.ktp.Basic()
key, pt = ktp.new_pair()
print(key)
print(pt)

target.simpleserial_write('p', pt)
ct = target.simpleserial_read('r', 16)
print(ct)

wave = cw.capture_trace(scope, target, pt).wave


smoothing = Smoothing.Smoothing()
medianFilter = MedianFilter.MedianFilter()
values = []  # Array to collect values
medianFilterValues = []
for value in wave:
    # Perform operations on each value
    print(value)
    value1 = smoothing.update(value)
    medianFilterValue = medianFilter.update(value)
    medianFilterValues.append(medianFilterValue)  # Collect value in array

    
curve = cw.plot(medianFilterValues).opts(fontscale=2, width=2000, height=1000, title='Analysis of Power Trace')
print(wave)

import panel as pn
bokeh_server = pn.Row(curve).show(port=12345)
bokeh_server.stop()


def reset_target(scope):
    scope.io.nrst = 'low'
    time.sleep(0.05)
    scope.io.nrst = 'high_z'
    time.sleep(0.05)

reset_target(scope)

# Debug print statement
print("Debug: Reset target completed")