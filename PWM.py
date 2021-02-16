import machine,utime

M1A = machine.PWM(machine.Pin(28))
M1B = machine.PWM(machine.Pin(27))
M1A.freq(80000000)
M1B.freq(80000000)
while(1):
    for i in range(0,65536):
        M1A.duty_u16(i)
    for i in range(0,65536):
        M1B.duty_u16(i)
        
        
        
