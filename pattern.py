from flask import Flask, jsonify, url_for, request, render_template
import RPi.GPIO as GPIO          
import time    

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
def ledOn(pin):
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)
    
def ledOff(pin):
    GPIO.output(pin,GPIO.LOW)
    return   

@app.route('/pattern', methods=['GET'])
def pattern():
    return render_template('pattern.html', mode=IO.getmode())


@app.route('/patonpin', methods=['POST'])
def patonpin():
    if request.method == 'POST':
        body=request.get_json()
        for i in range(0,5):
            
            ledOn(int(body.get('l1')))
            ledOn(int(body.get('l6')))
            time.sleep(2)
            ledOff(int(body.get('l1')))
            ledOff(int(body.get('l6')))
            time.sleep(0.5)
            ledOn(int(body.get('l2')))
            ledOn(int(body.get('l5')))
            time.sleep(1)
            ledOff(int(body.get('l2')))
            ledOff(int(body.get('l5')))
            time.sleep(0.5)
            ledOn(int(body.get('l3')))
            ledOn(int(body.get('l4')))
            time.sleep(2)
            ledOff(int(body.get('l3')))
            ledOff(int(body.get('l4')))
            time.sleep(0.5)
            ledOn(int(body.get('l2')))
            ledOn(int(body.get('l5')))
            time.sleep(1)
            ledOff(int(body.get('l2')))
            ledOff(int(body.get('l5')))
            time.sleep(0.5)
        return jsonify({"status" : body })
    else:
        return jsonify({'status:cant find status'})

@app.route("/cleanup", methods=["POST"])
def cleanup():
	if request.method == 'POST':
		IO.cleanup()
		return jsonify({"status": "Done cleaning the house!"})    

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')
