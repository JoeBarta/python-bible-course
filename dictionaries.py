students = {
    "Alice": ["ID001", 26, "A"],
    "Bob": ["ID002", 27, "B"],
    "Claire": ["ID003", 17, "C"],
    "Dan": ["ID004", 21, "D"],
    "Emma": ["ID005", 22, "E"]
    }


print(students["Claire"][0]) #get id
print(students["Dan"][0:1]) #age + Grade


# giving each key it's own dictionary as a value

new_students = {
    "Alice":{"id":"ID001","age":26, "grade":"A"},
    "Bob":{"id":"ID002","age":27, "grade":"B"},
    "Claire":{"id":"ID003","age":17, "grade":"C"},
    "Dan":{"id":"ID004","age":21, "grade":"D"},
    "Emma":{"id":"ID005","age":22, "grade":"E"}
    }

new_students(["Dan"]["age"])
new_students(["Emma"]["id"], new_students["Emma"]["grade"])
