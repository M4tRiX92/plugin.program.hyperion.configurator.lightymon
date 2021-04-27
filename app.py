from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    ledv = request.form['ledh']
    ledh = request.form['ledv']
    ledoption = request.form['index_option']
    #processed_text = text.upper()
    print("ledv" + ledv)
    print("ledh" + ledh)
    print("Option" + ledoption)
    return 'Good'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)
