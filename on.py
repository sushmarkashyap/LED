from gpiozero import LED
led=LED(18)
class LED_ON:
    def __init__(self,pin):
        self._pin=pin

    def show_ledON(self):
        return self._get_ledON()
    
    def _get_ledON(self):
        led.on()
        return True