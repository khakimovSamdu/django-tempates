from tinydb import TinyDB
import requests
td = TinyDB('db.json')
def get_brends():
    data = td.tables()
    return list(data)

def send_brend_all():
    data = get_brends()
    url = "http://127.0.0.1:8000/smartphone/add/"
    for item in data:
        brend = td.table(item).all()
        c = 0
        for value in brend:
            r = requests.post(url, json=value)
            print(r.status_code)
            c+=1
            if c>10:
                break
    return r.status_code
print(send_brend_all())
