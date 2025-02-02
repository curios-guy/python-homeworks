import random
import json
# import uuid

# print(uuid.uuid4())
def create_unique_id():
    try: 
        with open("id_data.txt", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    unique_id = random.randint(1000, 10000)

    
    while unique_id in data:
        unique_id = random.randint(1000, 10000)
        # print(unique_id)

    data.append(unique_id)

    with open("id_data.txt", "w") as file:
        json.dump(data, file)
    # print(unique_id, data)
    
    return unique_id

if __name__ == "__main__":
    create_unique_id()
    