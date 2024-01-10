import chipwhisperer as cw
import os
import time
import os

PLATFORM = 'CWNANO'

try:
    scope = cw.scope()
    target = cw.target(scope)
    prog = cw.programmers.STM32FProgrammer
except NameError:
    print("INFO: Unable to initialize USB connection. ?")

print("INFO: Found ChipWhisperer😍")

def reset_target(scope):
        scope.io.nrst = 'low'
        time.sleep(0.05)
        scope.io.nrst = 'high_z'
        time.sleep(0.05)

reset_target(scope)

base_path = "C:/Users/Senthil/ChipWhisperer5_64/cw/home/portable/chipwhisperer"
# firmware_path = "/hardware/victims/firmware/simpleserial-base-lab2/simpleserial-base-{}.hex".format(PLATFORM)
firmware_path = "/hardware/victims/firmware/basic-passwdcheck/basic-passwdcheck-{}.hex".format(PLATFORM)
full_path = os.path.normpath(base_path + firmware_path)
cw.program_target(scope, prog, full_path)

print("Programming Done")
