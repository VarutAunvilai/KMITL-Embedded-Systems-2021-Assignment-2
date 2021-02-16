import machine,utime
Alert = machine.Pin(0, machine.Pin.OUT)
Waterlevelsensor = machine.Pin(1,machine.Pin.IN,machine.Pin.PULL_DOWN)
Alert.value(0)
Button = machine.Pin(2,machine.Pin.IN,machine.Pin.PULL_UP)

def water_handler1(pin):
    print("Water level exceeded the limit")
    Alert.value(1)

def water_handler2(pin):
    Button.irq(handler=None)
    print("Water level did not exceeded the limit")
    Alert.value(0)
    Button.irq(trigger=machine.Pin.IRQ_FALLING,handler=water_handler2)


Waterlevelsensor.irq(trigger=machine.Pin.IRQ_RISING, handler=water_handler1)

Button.irq(trigger=machine.Pin.IRQ_FALLING,handler=water_handler2)

while True:
    pass
