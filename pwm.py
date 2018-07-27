from flask import Flask, jsonify, request, render_template,url_for
import RPi.GPIO as GPIO   
import time                            

GPIO.setwarnings(False)   
IO.setmode (IO.BCM) 
app = Flask(__name__)       
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

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')