from flask import Flask, request, jsonify, render_template, url_for
import RPi.GPIO as IO

app = Flask(__name__)
IO.setmode(IO.BCM)

def onLED(pin):
	IO.setup(pin, IO.OUT)
	IO.output(pin, IO.HIGH)
	return 'LED no: {} ON'.format(str(pin))

def offLED(pin):
	IO.setup(pin, IO.OUT)
	IO.output(pin, IO.LOW)
	return 'LED no: {} OFF'.format(str(pin))


# Route "/" -> GET -> templates/led.html => Display Button for on-off & ask for pin number from the user. 
# Route "/on" -> POST => Get the pin and on or off led using RPI.
# Route "/off" -> POST => Get the pin and on or off led using RPI.
@app.route("/", methods=["GET"])
def led():
	if request.method == 'GET':
		return render_template('traffic.html', mode=IO.getmode())

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

    
@app.route("/cleanup", methods=["POST"])
def cleanup():
	if request.method == 'POST':
            IO.cleanup()
            return jsonify({"status": "Done cleaning the house!"})

# Route "/pwm" -> GET -> templates/pwm.html => Display Button for on-off & ask for pin number & duty cycle from the user. 
# Route "/pwm" -> POST => Get the pin & duty cycle, on or off led using RPI and then change the intensity of light.

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
