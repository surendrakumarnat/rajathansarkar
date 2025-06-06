from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('formcode.html')

@app.route('/submit', methods=['POST'])
def submit():
    fullname = request.form['fullname']
    age = request.form['age']
    mobile = request.form['mobile']
    whatsapp = request.form['whatsapp']
    gmail = request.form['gmail']
    education = request.form['education']
    id_type = request.form['idType']

    pdf_file = request.files['rusemPdf']
    if pdf_file:
        upload_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
        pdf_file.save(upload_path)

    with open('registrations.txt', 'a') as f:
        f.write(f"{fullname}, {age}, {mobile}, {whatsapp}, {gmail}, {education}, {id_type}, {pdf_file.filename}\n")

    return f"<h2>Thank you {fullname}, your data has been submitted successfully!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
