from flask import Flask, jsonify, url_for, request, render_template
from gpiozero import LED
import time


app = Flask(__name__)
led1=LED(14)
led2=LED(15)
led3=LED(18)
led4=LED(2)
led5=LED(3)
led6=LED(4)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/onpin', methods=['POST'])
def onpin():
    if request.method == 'POST':
        body=request.get_json()
        for i in range(0, 5):
            led1.on()
            time.sleep(0.25)
            led2.0n()
            time.sleep(0.5)
            led1.off()
            led2.off()
            time.sleep(0.25)
             led3.on()
            time.sleep(0.25)
            led4.0n()
            time.sleep(0.5)
            led3.off()
            led4.off()
            time.sleep(0.25)
             led5.on()
            time.sleep(0.25)
            led6.0n()
            time.sleep(0.5)
            led5.off()
            led6.off()
            time.sleep(0.25)
            led1.on()
            led3.on()
            led5.on()
            time.sleep(0.5)
            led1.off()
            led3.off()
            led5.off()
            time.sleep(0.25)
            led2.on()
            led4.on()
            led6.on()
            time.sleep(0.5)
            led2.off()
            led4.off()
            led6.off()
            time.sleep(0.25)
        return jsonify({"status" : 'on.show_ledON()' })
    else:
         return jsonify({'status:cant find status'})
    
if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')
