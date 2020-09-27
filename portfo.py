from flask import Flask, render_template
from flask.globals import request
import csv

app = Flask(__name__)


@app.route('/')
def index():
    """
    Route to index.html
    """
    return render_template('index.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database2.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # in html, in the form tag, set action to name of route, in this case, 'submit_form'
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            # print(data)
            write_to_csv(data)
            return 'form submitted'
        except:
            return 'was not saved to database'
    else:
        return 'something went wrong'
