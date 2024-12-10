from flask import Flask, request, jsonify
from tinydb import TinyDB
import re
from datetime import datetime


app = Flask(__name__)
db = TinyDB('forms_db.json')


def get_email(value):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value))

def get_phone(value):
    return bool(re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value))

def get_date(value):
    try:
        if re.match(r'^\d{2}\.\d{2}\.\d{4}$', value):
            datetime.strptime(value, '%d.%m.%Y')
        elif re.match(r'^\d{4}-\d{2}-\d{2}$', value):
            datetime.strptime(value, '%Y-%m-%d')
        else:
            return False
        return True
    except ValueError:
        return False

def check_field_type(value):
    if get_date(value):
        return "date"
    elif get_phone(value):
        return "phone"
    elif get_email(value):
        return "email"
    else:
        return "text"


@app.route('/get_form', methods=['POST'])
def get_form():
    form_data = request.form.to_dict()
    templates = db.all()

    for template in templates:

        match = True
        for field_name, field_type in template['fields'].items():

            if field_name == "name":
                continue

            if field_name not in form_data or check_field_type(form_data[field_name]) != field_type:
                match = False
                break

        if match:
            return jsonify({"template_name": template["name"]})


    response = {}
    for field_name, value in form_data.items():
        response[field_name] = check_field_type(value)

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
