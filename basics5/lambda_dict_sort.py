some_dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
             {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
             {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

print(sorted(some_dict, key= lambda x: x['make']))
print(sorted(some_dict, key= lambda x: x['color']))
# print(sorted(some_dict, key= lambda x: x['model'])) - Error - str and int not sorted
