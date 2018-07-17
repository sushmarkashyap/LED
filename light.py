from on import LED_ON
from off import LED_OFF

pin_on = LED_ON(True, 6)
print(pin_on.show_ledON())
print(pin_on.show_pinON())
pin_off = LED_OFF(False,5)
print(pin_off.show_ledOFF())
print(pin_off.show_pinOFF())
