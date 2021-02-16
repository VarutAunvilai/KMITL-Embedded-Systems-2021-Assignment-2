import machine,utime
Alert = machine.Pin(0, machine.Pin.OUT)
Touchsensor = machine.Pin(1,machine.Pin.IN,machine.Pin.PULL_DOWN)
Alert.value(0)
Button = machine.Pin(2,machine.Pin.IN,machine.Pin.PULL_UP)

def touch_handler1(pin):
    print("Touched")
    Alert.value(1)

def touch_handler2(pin):
    Button.irq(handler=None)
    print("Reset")
    Alert.value(0)
    Button.irq(trigger=machine.Pin.IRQ_FALLING,handler=touch_handler2)


Touchsensor.irq(trigger=machine.Pin.IRQ_RISING, handler=touch_handler1)

Button.irq(trigger=machine.Pin.IRQ_FALLING,handler=touch_handler2)

while True:
    pass

