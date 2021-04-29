from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_Lightymon():
    return 'Welcome to Lightymon!'

@app.route('/setleds')
def my_form():
    return render_template('form.html')

@app.route('/setleds', methods=['POST'])
def my_form_post():
    ledv = request.form['ledv']
    ledh = request.form['ledh']
    direction = request.form['direction']
    device = request.form['device']
    center_corner = request.form['center_corner']
    processed_text = "ledv " + ledv + " - ledh " + ledh + " - direction " + direction + " - device " + device + " - center_corner " + center_corner
    #setEverything(ledh, ledv, options)
    return processed_text

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)
