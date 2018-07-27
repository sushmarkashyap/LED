from flask import Flask, request, jsonify, render_template, url_for
import RPi.GPIO as GPIO
import time
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

def onLED(pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)
	return 'LED no: {} ON'.format(str(pin))

def offLED(pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	return 'LED no: {} OFF'.format(str(pin))


# Route "/" -> GET -> templates/led.html => Display Button for on-off & ask for pin number from the user. 
# Route "/on" -> POST => Get the pin and on or off led using RPI.
# Route "/off" -> POST => Get the pin and on or off led using RPI.
@app.route("/", methods=["GET"])
def led():
	if request.method == 'GET':
		return render_template('led.html', mode=GPIO.getmode())

@app.route("/onpin", methods=["POST"])
def led_on():
	if request.method == 'POST':
		body = request.get_json()
        onLED(int(body.get('led')))
        return jsonify({"status": body})

@app.route("/offpin", methods=["POST"])
def led_off():
	if request.method == 'POST':
		body = request.get_json()
		offLED(int(body.get('led')))
		return jsonify({"status": body})
        GPIO.cleanup()



# Route "/pwm" -> GET -> templates/pwm.html => Display Button for on-off & ask for pin number & duty cycle from the user. 
# Route "/pwm" -> POST => Get the pin & duty cycle, on or off led using RPI and then change the intensity of light.

@app.route('/pwm', methods=['GET'])
def pwm():
    return render_template('PWM.html', mode=GPIO.getmode())

@app.route('/pwmon', methods=['POST'])
def pwmon():
    if request.method == 'POST':
        body=request.get_json()
        GPIO.setup(int(body.get('l1')),GPIO.OUT)
        p = GPIO.PWM(int(body.get('l1')),100) 
        p.start(0)                              
        try:
            for i in range(5):
                for x in range (50):                         
                    p.ChangeDutyCycle(x)              
                    time.sleep(0.1)                           
            
                for x in range (50):                        
                    p.ChangeDutyCycle(50-x)        
                    time.sleep(0.1)
        except KeyboardInterrupt:
            pass
        p.stop()
        GPIO.cleanup()
        return jsonify({"status" : body })  
    else:
        return jsonify({'status:cant find status'})

# Route "/pwm" -> GET -> templates/pwm.html => Display Button for on-off & ask for pin number & duty cycle from the user. 
# Route "/pwm" -> POST => Get the pin & duty cycle, on or off led using RPI and then change the intensity of light.

@app.route("/traffic", methods=["GET"])
def traffic():
	if request.method == 'GET':
		return render_template('traffic.html', mode=GPIO.getmode())

@app.route("/redonpin", methods=["POST"])
def rled_on():
	if request.method == 'POST':
		body = request.get_json()
        onLED(int(body.get('red')))
        return jsonify({"status": body})

@app.route("/redoffpin", methods=["POST"])
def rled_off():
	if request.method == 'POST':
		body = request.get_json()
		offLED(int(body.get('red')))
		return jsonify({"status": body})
        GPIO.cleanup()

@app.route("/yelonpin", methods=["POST"])
def yled_on():
	if request.method == 'POST':
		body = request.get_json()
        onLED(int(body.get('yel')))
        return jsonify({"status": body})

@app.route("/yeloffpin", methods=["POST"])
def yled_off():
	if request.method == 'POST':
		body = request.get_json()
		offLED(int(body.get('yel')))
		return jsonify({"status": body})
        GPIO.cleanup()

@app.route("/greonpin", methods=["POST"])
def gled_on():
	if request.method == 'POST':
		body = request.get_json()
        onLED(int(body.get('gre')))
        return jsonify({"status": body})

@app.route("/greoffpin", methods=["POST"])
def gled_off():
	if request.method == 'POST':
		body = request.get_json()
		offLED(int(body.get('gre')))
		return jsonify({"status": body})
        GPIO.cleanup() 

# Route "/pwm" -> GET -> templates/pwm.html => Display Button for on-off & ask for pin number & duty cycle from the user. 
# Route "/pwm" -> POST => Get the pin & duty cycle, on or off led using RPI and then change the intensity of light.

@app.route('/pattern', methods=['GET'])
def pattern():
    return render_template('pattern.html', mode=GPIO.getmode())


@app.route('/patonpin', methods=['POST'])
def patonpin():
    if request.method == 'POST':
        body=request.get_json()
        for i in range(0,5):
            
            onLED(int(body.get('l1')))
            onLED(int(body.get('l6')))
            time.sleep(2)
            offLED(int(body.get('l1')))
            offLED(int(body.get('l6')))
            time.sleep(0.5)
            onLED(int(body.get('l2')))
            onLED(int(body.get('l5')))
            time.sleep(1)
            offLED(int(body.get('l2')))
            offLED(int(body.get('l5')))
            time.sleep(0.5)
            onLED(int(body.get('l3')))
            onLED(int(body.get('l4')))
            time.sleep(2)
            offLED(int(body.get('l3')))
            offLED(int(body.get('l4')))
            time.sleep(0.5)
            onLED(int(body.get('l2')))
            onLED(int(body.get('l5')))
            time.sleep(1)
            offLED(int(body.get('l2')))
            offLED(int(body.get('l5')))
            time.sleep(0.5)
        return jsonify({"status" : body })
        GPIO.cleanup()
    else:
        return jsonify({'status:cant find status'})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')