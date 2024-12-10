from tinydb import TinyDB

db = TinyDB('forms_db.json')


db.insert({
    "name": "Order Form",
    "fields": {
        "f_name1": "email",
        "f_name2": "phone",
        "f_name3": "date"
    }
})
db.insert({
    "name": "Registration Form",
    "fields": {
        "user_email": "email",
        "user_phone": "phone",
        "registration_date": "date"
    }
})
