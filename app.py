from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    return 'You entered: {}'.format(request.form['text'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)