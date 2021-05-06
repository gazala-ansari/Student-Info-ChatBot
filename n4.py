from pymongo import MongoClient
client =MongoClient("mongodb+srv://Gazala:Gazala%40123@cluster0.nhjog.mongodb.net/chatbot?retryWrites=true&w=majority")
db = client.test
db=client.get_database('chatbot')
record=db.Exam
#print(record.find_one({"dept":"computers"},{"subject":1}))
oo=record.find_one({"dept":"computers"},{"subject":1})
oo.pop('_id')
print(oo)
