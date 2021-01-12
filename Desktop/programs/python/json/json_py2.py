import json

# list to Array (json)
print(json.dumps(['Harsh', '12', ['python', 'html']]))

# tuple to array (json)
print(json.dumps(("Harsh", "12", ["python", "html"])))

# string to String (json)
print(json.dumps("Harsh"))

# int to Number (json)
print(json.dumps(12))

# float to Number (json)
print(json.dumps(12.03))

# Boolean to their respective values
print(json.dumps(True))
print(json.dumps(False))

# None value to null
print(json.dumps(None))


