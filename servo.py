from flask import Flask, jsonify, request, render_template,url_for
import RPi.GPIO as IO   
import time                            

IO.setwarnings(False)   
IO.setmode (IO.BCM) 
app = Flask(__name__)       
@app.route('/', methods=['GET'])
def index():
    return render_template('servo.html', mode=IO.getmode())

@app.route('/onpin', methods=['POST'])
def onpin():
    if request.method == 'POST':
        body=request.get_json()
        IO.setup(int(body.get('l1')),IO.OUT)
        p = IO.PWM(int(body.get('l1')),50) 
        p.start(7.5)
        try:
            for i in range(0,3):
                print("entering loop")
                p.ChangeDutyCycle(float(body.get('l2')))  
                time.sleep(1)
                p.ChangeDutyCycle(7.5) 
                time.sleep(1)            
        except KeyboardInterrupt:
            pass
        return jsonify({"status" : body })
        p.stop() 
        IO.cleanup()   
    else:
        return jsonify({'status:cant find status'})    



if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')