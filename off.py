from gpiozero import LED

class LED_OFF:
    def __init__(self,pin):
        self._pin=pin

    def show_ledOFF(self):
        return self._get_ledOFF()
        
    def _get_ledOFF(self):
        led=LED(18)
        led.off()
        return True

    