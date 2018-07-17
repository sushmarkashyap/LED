from gpiozero import LED
led=LED(17)
class LED_OFF:
    def __init__(self,pin):
        self._pin=pin

    def show_ledOFF(self):
        return self._get_ledOFF()
        
    def _get_ledOFF(self):
        led.off()
        return True

    