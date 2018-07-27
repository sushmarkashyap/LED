from flask import Flask, request, jsonify, render_template, url_for
import RPi.GPIO as GPIO

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

@app.route("/cleanup", methods=["POST"])
def cleanup():
	if request.method == 'POST':
		GPIO.cleanup()
        return jsonify({"status": "Done cleaning the house!"})

# Route "/pwm" -> GET -> templates/pwm.html => Display Button for on-off & ask for pin number & duty cycle from the user. 
# Route "/pwm" -> POST => Get the pin & duty cycle, on or off led using RPI and then change the intensity of light.

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')