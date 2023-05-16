students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]

def iterateDictionary2(key_name, some_list):
    for x in some_list:
        print(x[key_name])
print(iterateDictionary2("last_name",students))