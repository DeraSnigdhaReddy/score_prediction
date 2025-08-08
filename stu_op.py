import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db=client["Demo_practise"]
collection=db["practise"]

print(list(collection.find()))

# q=input("want to update(yes/no)")

# if q=="yes":
#     w=input("Which u want to update ")
#     a=input("which person name:")
#     n=input("What is the update value:")
#     #u_a=input("what is the updated age:")
#     collection.update_one({"Name":a},{"$set":{w:n}})

# q=input("U want to delete(yes/no):")
# if q=="yes":
#     w=input("Which u want to delete:")
#     a=input("Which name u wnat to delete:")
    
#     collection.delete_one({w:a})
s=input("What u want to search:")
w=input("Name:")
print(collection.find_one({s:w}))
