import demjson
import json



# decoding using demjson package
var = '{"Name":"Harsh", "Age":12, "languages":"python"}'

text = demjson.decode(var)
print(text)
