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
    options = request.form['options']
    processed_text = ledv.upper()
    print("ledv " + ledv + " - ledh " + ledh + " - option " +options)
    return processed_text

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)
