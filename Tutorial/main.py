from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

import os
import pprint


load_dotenv(find_dotenv())

password = os.environ.get('MONGODB_PWD')

connection_string = f"mongodb+srv://abylai-aitbanov:{password}@tutorialtim.3n61r.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

dbs = client.list_database_names()
test_db = client['test']
collections = test_db.list_collection_names()
# print(collections)


def insert_test_doc():
    collection = test_db.test
    test_document = {
        'name': 'Abylai',
        'type': 'Test'
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)
    # client.test.test.insert(test_document)


production = client.production
person_collection = production.person_collection


def create_documents():
    first_names = ['Tim', 'John', 'Clark', 'James', 'Mark']
    last_names = ['Smith', 'Pit', 'Geral', 'Bart', 'JR']
    ages = [23, 26, 27, 28, 29]

    docs = []

    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {'first_name': first_name, 'last_name': last_name, 'age': age}
        # person_collection.insert_one(doc)
        docs.append(doc)
    person_collection.insert_many(docs)


printer = pprint.PrettyPrinter()


def find_all_people():
    people = person_collection.find()
    # print(list(peeople))
    for person in people:
        printer.pprint(person)


def find_tim():
    tim = person_collection.find_one(
        {"first_name": "Tim", "last_name": "Smith"})
    printer.pprint(tim)


def count_all_people():
    count = person_collection.count_documents(filter={})
    #  .find().count()
    print(f"Number of people {count}")


def get_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)
    person = person_collection.find_one({'_id': _id})
    printer.pprint(person)


def get_age_range(min_age, max_age):
    query = {"$and": [{"age": {"$gte": min_age}},
                      {"age": {"$lte": max_age}}, ]}

    people = person_collection.find(query).sort("age")
    for person in people:
        printer.pprint(person)


def project_columns():
    columns = {"_id": 0, "first_name": 1, "last_name": 1}  # or just {"_id": 0}
    people = person_collection.find({}, columns)
    for person in people:
        printer.pprint(person)


def update_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)
    all_updates = {
        "$set": {"new_field": True},
        "$inc": {"age": 1},
        "$rename": {"first_name": "first", "last_name": "last"}
    }
    person_collection.update_one({"_id": _id}, all_updates)
    # person_collection.update_one({"_id": _id}, {"$unset": {"new_field": ""}})


def replace_one(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)

    new_doc = {
        "first_name": "new first name",
        "last_name": "new last name",
        "age": 100
    }
    person_collection.replace_one({"_id": _id}, new_doc)


def delete_doc_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)
    person_collection.delete_one({"_id": _id})


address = {
    "_id": "62b85835fffcc3ff5b32",
    "street": "New Street",
    "number": 234,
    "country": "United States",
    "zip": 231
}


def add_address_embed(person_id, address):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)

    person_collection.update_one(
        {"_id": _id}, {"$addToSet": {"adresses": address}})


add_address_embed('62b85835fffcc3ff5b32a75c', address)
