import json

def load_db():
    with open("flashcard_db.json") as f:
        return json.load(f)


## after reading the whole json 
## variable db has the question 
## now we can add element in the list of db
## then when save we dump it in the same file
## so new data will persist
def save_db():
    with open("flashcard_db.json","w") as f:
        return json.dump(db,f)

db = load_db()