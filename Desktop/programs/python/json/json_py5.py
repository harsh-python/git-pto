import json

office_string = """
{
"emp":[
{
"emp_name":"Tim",
"emp_sal":"20000",
"emp_email":["tim20522@dummyemail.com"]
},
{
"emp_name":"Harsh",
"emp_sal":"21000",
"emp_email":["null"]
}
]
}
"""

data = json.loads(office_string)
# printing data
#print(data)

# finding is it a python data type
#print(type(data))

# finding a list in data
#print(type(data["emp"]))

# finding the name and email in data
# using (for loop)
for office_data in data["emp"]:
    print(office_data['emp_name'], office_data['emp_email'])

