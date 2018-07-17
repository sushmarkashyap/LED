from flask import Flask, jsonify, url_for, request, render_template
from gpiozero import LED
#from on import LED_ON
#from off import LED_OFF


app = Flask(__name__)
led=LED(18)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/onpin', methods=['POST'])
def onpin():
    if request.method == 'POST':
        body=request.get_json()
        # on = LED_ON(body['pin'])
        led.on()
        return jsonify({"status" : on.show_ledON() })
    else:
         return jsonify({'status:cant find status'})
    
@app.route('/offpin', methods=['POST'])
def offpin():
    if request.method == 'POST':
        body=request.get_json()
        # off = LED_OFF(body['pin'])
        led.off()
        return jsonify({"status" : off.show_ledOFF() })
    else:
        return jsonify({'status:cant find status'})          
    
if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')
