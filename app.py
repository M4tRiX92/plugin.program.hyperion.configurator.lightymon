from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setleds')
def my_form():
    return render_template('setleds.html')

@app.route('/setleds', methods=['GET', 'POST'])
def my_form_post():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        ledv = request.form['ledv']
        ledh = request.form['ledh']
        direction = request.form['direction']
        device = request.form['device']
        center_corner = request.form['center_corner']
        processed_text = "ledv " + ledv + " - ledh " + ledh + " - direction " + direction + " - device " + device + " - center_corner " + center_corner
        #setEverything(ledh, ledv, options)
        return processed_text

    # show the form, it wasn't submitted
    return render_template('setleds.html')
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)