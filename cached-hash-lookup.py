from datetime import datetime

people = [
    {
        "name": "Bob",
        "amount": 123.50
    },
    {
        "name": "Carol",
        "amount": 223.50
    },
    {
        "name": "Ted",
        "amount": 313.50
    },
    {
        "name": "Alice",
        "amount": 423.50
    },
]
for _ in range(9999):
    people.insert(0,  {
        "name": "Bob",
        "amount": 123.50
    })

#print(people[2]["amount"])

# create a dict of objects from a list of object
faster_people = {}

#TODO fill the dict with objects from list
print("DO TRANSFORMATION")
start = datetime.now()
for item in people:
    id_value = item["name"]
    faster_people[id_value] = item
print((datetime.now() - start).total_seconds()*1000)

#quick access
print(faster_people["Ted"]["amount"])

#slow lookup
def slow_find():
    for p in people:
        if p["name"] == "Ted":
            return p["amount"]
    return None

print("SLOW FIND 1")
start = datetime.now()
print(slow_find())
print((datetime.now() - start).total_seconds()*1000)

#faster
def faster_find():
    return faster_people["Ted"]["amount"]

print("FAST FIND 1")
start = datetime.now()
print(faster_find())
print((datetime.now() - start).total_seconds()*1000)

print("FAST FIND 2")
start = datetime.now()
print(faster_find())
print((datetime.now() - start).total_seconds()*10000)

