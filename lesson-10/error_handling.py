import csv

# class ValidationError(Exception):
#     """Exception Raised for validation errors."""
#     def __init__(self, field, message, *args):
#         self.field = field
#         self.message = message
#         super().__init__(*args);

# try:
#     raise ValidationError("username", "must not be empty")
# except ValueError as e: 
#     print(e)

with open("usernames.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    columns = next(reader)
    for row in reader:
        print(row)

columns = ["Username", "Name", "Age"]
data = [
        ["Salom", "Dareqqqq", 12],
        ["Wassup", "asdasd", 123]
    ]


with open("database.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(data)

with open("database.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=",")
    rows = list(reader)
    
    print(rows)

# data = [
#     {"Username": "Hello", "Name": "Damn", "Age": "12", }
# ]
# fieldnames = ["Username", "Name", "Age"]
# file = open("databse.csv", "w", newline="")
# writer = csv.DictWriter(file, fieldnames=fieldnames)
# writer.writeheader()
# writer.writerows(data)

from datetime import datetime
import json
data = {
    "Name": "strange",
    "Date": datetime.now()
}
class DateEncodder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

print(json.dumps(data, cls = DateEncodder))