import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db=client["Demo_practise"]
collection=db["practise"]

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter the Student name: ")
    age = int(input("Enter the Student age: "))
    roll = int(input("Enter the Student roll: "))
    phone = int(input("Enter the Student phone: "))
    address = input("Enter the Student address: ")
    collection.insert_one({
        "Name":name,
        "Age": age,
        "Roll": roll,
        "Phone":phone,
        "Address": address
    })
