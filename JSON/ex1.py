import json

x={ "name":"kishore", "age":"20", "color":"brown", "love":False }
y=json.dumps(x,indent=4,separators=(". "," = "),sort_keys=True)
print(y)
print(json.dumps(("apple","orange")))
print(json.dumps(["apple","banana"]))
print(json.dumps(21))
print(json.dumps(21.3))
print(json.dumps(None))

#-------------------------------------------------------------------------------------------------

A='{"name":"kishore","age":"20","color":"20","love":"False"}'
B=json.loads(A)
print(B)
print(type(B))