import json

data = {"name": "Mary A. Python", "email": "marry123@python.org"}
json_string = json.dumps(data)
print(json_string)

d = json.loads(json_string)
print(d == data)  # True
