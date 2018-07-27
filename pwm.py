from flask import Flask, jsonify, request, render_template,url_for
import RPi.GPIO as IO   
import time                            

IO.setwarnings(False)   
IO.setmode (IO.BCM) 
app = Flask(__name__)       
@app.route('/', methods=['GET'])
def index():
    return render_template('PWM.html', mode=IO.getmode())

@app.route('/onpin', methods=['POST'])
def onpin():
    if request.method == 'POST':
        body=request.get_json()
        IO.setup(int(body.get('l1')),IO.OUT)
        p = IO.PWM(int(body.get('l1')),100) 
        p.start(0)                              
        try:
            while 1:
                for x in range (50):                         
                    p.ChangeDutyCycle(x)              
                    time.sleep(0.1)                           
            
                for x in range (50):                        
                    p.ChangeDutyCycle(50-x)        
                    time.sleep(0.1)
        except KeyboardInterrupt:
            pass
        p.stop()
        IO.cleanup()
        return jsonify({"status" : body })  
    else:
        return jsonify({'status:cant find status'})    

@app.route('/offpin', methods=['POST'])
def offpin():
    if request.method == 'POST':
        body=request.get_json()
        IO.output(int(body.get('l1')),IO.LOW)
        return jsonify({"status" : body })

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')