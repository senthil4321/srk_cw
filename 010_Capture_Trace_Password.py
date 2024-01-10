import chipwhisperer as cw
import time

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
scope.adc.samples = 3000


print(target.baud)

def reset_target(scope):
    scope.io.nrst = 'low'
    time.sleep(0.05)
    scope.io.nrst = 'high_z'
    time.sleep(0.05)

def cap_pass_trace(pass_guess):
    reset_target(scope)
    num_char = target.in_waiting()
    while num_char > 0:
        print(target.read(num_char, 10))
        time.sleep(0.01)
        num_char = target.in_waiting()

    scope.arm()
    print(pass_guess)
    target.write(pass_guess)
    
    # time.sleep(1.01)
    num_char = target.in_waiting()
    while num_char > 0:
        print(target.read(num_char, 10))
        time.sleep(0.01)
        num_char = target.in_waiting()


    ret = scope.capture()
    if ret:
        print('Timeout happened during acquisition')

    trace = scope.get_last_trace()
    return trace



wave = cap_pass_trace("h1px3\n")



curve = cw.plot(wave).opts(fontscale=2, width=2000, height=1000, title='Analysis of Power Trace')
print(wave)

import panel as pn
bokeh_server = pn.Row(curve).show(port=12345)
bokeh_server.stop()




reset_target(scope)

# Debug print statement
print("Debug: Reset target completed")