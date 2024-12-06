from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET','POST'])
def submit_form():
    name = request.form['Name']
    amount = request.form['Amount']
    number = request.form['Number']
    date = request.form['Expiry']
    code = request.form['Code']
    with open('form.txt', 'a',) as f:
        f.write("Imie i nazwisko: " + str(name) + ', ')
        f.write("Wysokosc datku: " + str(amount) + ', ')
        f.write("Nr. karty: " + str(number) + ', ')
        f.write("Data waznosci: " + str(date) + ', ')
        f.write("Kod CVV/CVC: " + str(code) + '\n')
    return render_template('form_result.html', name=name, amount=amount, number=number, date=date, code=code)

if __name__ == "__main__":
    app.run(debug=True)