import json
from pathlib import Path

import addressbook_pb2


N = 1000000

address_book = addressbook_pb2.AddressBook()

for i in range(N):
	person = address_book.people.add()
	person.id = i
	person.name = "John Doe"
	person.email = "jdoe@example.com"
	phone = person.phones.add()
	phone.number = "555-4321"
	phone.type = addressbook_pb2.Person.HOME

serialized = address_book.SerializeToString()

with open('result.bin', 'wb') as out_file:
	out_file.write(serialized)

with open('result.bin', 'rb') as in_file:
	deserialized = addressbook_pb2.AddressBook()
	deserialized.ParseFromString(in_file.read())

print(deserialized.people[0])

address_book_dict = [
	{
		'id': i,
		'name': 'John Doe',
		'email': 'jdoe@example.com',
		'phones': [
			{
				'number': '555-4321',
				'type': 1
			}
		]
	} for i in range(N)
]

with open('result.json', 'w') as out_file:
	out_file.write(json.dumps(address_book_dict))

with open('result.json', 'r') as in_file:
	address_book = json.loads(in_file.read())
print(address_book[0])

def get_file_size(file_path):
   """ Get size of file at given path in bytes"""
   # get file object
   file_obj = Path(file_path)
   # Get file size from stat object of file
   size = file_obj.stat().st_size
   return size

for filepath in ('result.bin', 'result.json'):
	print(f"File size of '{filepath}' is {get_file_size(filepath) / 1024 / 1024:.2f} MB.")

# File size of 'result.bin' is 45.76 MB.
# File size of 'result.json' is 106.71 MB.