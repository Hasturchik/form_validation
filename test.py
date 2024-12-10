import requests

# URL вашего Flask-приложения
url = "http://127.0.0.1:5000/get_form"

"""
Подходит под имеющийся щаблон
"""
data_1 = {
    "f_name1": "john.doe@example.com",
    "f_name2": "+7 123 456 78 90",
    "f_name3": "12.12.2024"
}

response_1 = requests.post(url, data=data_1)
print("Response 1:", response_1.json())

"""
Не подходит под имеющийся щаблон
"""
data_2 = {
    "name": "Jane Doe",
    "email": "jane.doe",
    "phone": "1234567890",
    "date": "2024-12-12"
}

response_2 = requests.post(url, data=data_2)
print("Response 2:", response_2.json())
