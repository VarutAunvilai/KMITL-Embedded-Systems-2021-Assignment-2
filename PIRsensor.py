import machine,utime
Alert = machine.Pin(0, machine.Pin.OUT)
PIRsensor = machine.Pin(1,machine.Pin.IN,machine.Pin.PULL_DOWN)
Alert.value(0)


def PIR_handler(pin):
    print("motion detected")
    Alert.value(1)
    utime.sleep(1)
    Alert.value(0)
    utime.sleep(1)
    
PIRsensor.irq(trigger=machine.Pin.IRQ_RISING, handler=PIR_handler)

while True:
    pass