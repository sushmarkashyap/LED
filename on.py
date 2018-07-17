from gpiozero import LED

class LED_ON:
    def __init__(self,pin):
        self._pin=pin

    def show_ledON(self):
        return self._get_ledON()
    
    def _get_ledON(self):
        led=LED(18)
        led.on()
        return True