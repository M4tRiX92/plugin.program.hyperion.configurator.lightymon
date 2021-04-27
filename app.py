from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['ledv']
    processed_text = text.upper()
    print(processed_text)
    return processed_text

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)
