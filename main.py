from flask import Flask, jsonify, url_for, request, render_template
import RPi.GPIO as GPIO          
import time    

app = Flask(__name__)

def ledOn(pin,tiim):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(tiim)
def ledOff(pin,tiim):
    GPIO.output(pin,GPIO.LOW)
    time.sleep(tiim) 
    return   

@app.route('/', methods=['GET'])
def index():
    return render_template('pattern.html', mode=GPIO.getmode())

@app.route('/pin1', methods=['POST'])
def pin1():
    if request.method == 'POST':
        body=request.get_json()
        red1=GPIO.setup(body['led1'],IO.OUT)
        return jsonify({"status" :' pin1 entered' })
    else:
        return jsonify({'status:cant find status'})
        
   
@app.route('/pin2', methods=['POST'])
def pin2():
     if request.method == 'POST':
        body=request.get_json()
        yellow1=GPIO.setup(body['led2'],IO.OUT)
        return jsonify({"status" :' pin2 entered' })
    else:
        return jsonify({'status:cant find status'})
       
@app.route('/pin3', methods=['POST'])
def pin3():
     if request.method == 'POST':
        body=request.get_json()
        green1=GPIO.setup(body['led3'],IO.OUT)
        return jsonify({"status" :' pin3 entered' })
    else:
        return jsonify({'status:cant find status'})
        
  
@app.route('/pin4', methods=['POST'])
def pin4():
    if request.method == 'POST':
        body=request.get_json()
        red2=GPIO.setup(body['led4'],IO.OUT)
        return jsonify({"status" :' pin4 entered' })
    else:
        return jsonify({'status:cant find status'})
        
    
@app.route('/pin5', methods=['POST'])
def pin5():
     if request.method == 'POST':
        body=request.get_json()
       yellow2=GPIO.setup(body['led5'],IO.OUT)
        return jsonify({"status" :' pin5 entered' })
    else:
        return jsonify({'status:cant find status'})
        
   
@app.route('/pin6', methods=['POST'])
def pin6():
     if request.method == 'POST':
        body=request.get_json()
        green2=GPIO.setup(body['led6'],IO.OUT)
        return jsonify({"status" :' pin6 entered' })
    else:
        return jsonify({'status:cant find status'})
        


@app.route('/onpin', methods=['POST'])
def onpin():
    if request.method == 'POST':
        body=request.get_json()
        for i in range(0,5):
            ledOn(red1,2)
            ledOn(green2,2)
            ledOff(red1,0.5)
            ledOff(green2,0.5)
            ledOn(yellow1,1)
            ledOn(yellow2,1)
            ledOff(yellow1,0.5)
            ledOff(yellow2,0.5)
            ledOn(red2,2)
            ledOn(green1,2)
            ledOff(red2,0.5)
            ledOff(green1,0.5)
            ledOn(yellow1,1)
            ledOn(yellow2,1)
            ledOff(yellow1,0.5)
            ledOff(yellow2,0.5)
        return jsonify({"status" : 'on.show_ledON()' })
    else:
        return jsonify({'status:cant find status'})

@app.route("/cleanup", methods=["POST"])
def cleanup():
	if request.method == 'POST':
		GPIO.cleanup()
		return jsonify({"status": "Done cleaning the house!"})    

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')
