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
prog = cw.programmers.STM32FProgrammer
time.sleep(0.05)
scope.default_setup()

def reset_target(scope):
        scope.io.nrst = 'low'
        time.sleep(0.05)
        scope.io.nrst = 'high_z'
        time.sleep(0.05)

reset_target(scope)

