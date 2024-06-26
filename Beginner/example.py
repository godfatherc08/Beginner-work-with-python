import json


person = {
    "name":"Desmond",
    "age": 16,
    "city": "New York",
    "children": False,
    "titles": ["king", "chief", "general"]
}

personjson = json.dumps(person, indent=4, separators=(',', ':'))
print(personjson)
