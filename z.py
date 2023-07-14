keys = ['rollno','name','sub']
values = [1,'xyz','maths']

result = {key: value for key, value in zip(keys, values)}
print(result)


keys = list(my_dict.keys())
values = list(my_dict.values())

print(keys)
print(values)