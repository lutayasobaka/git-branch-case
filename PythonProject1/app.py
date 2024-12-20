from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'секретный_ключ'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        surname = request.form['surname']
        name = request.form['name']
        patronymic = request.form['patronymic']
        full_name = f"{surname} {name} {patronymic}"
        return redirect(url_for('greeting', full_name=full_name))
    return render_template('index.html')

@app.route('/greeting/<full_name>', methods=['GET'])
def greeting(full_name):
    return render_template('greeting.html', full_name=full_name)

@app.route('/exit/<full_name>', methods=['GET', 'POST'])
def exit(full_name):
    if request.method == 'POST':
        return render_template('exit.html', full_name=full_name)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)