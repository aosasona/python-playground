from database import cursor, db

#Ask what the user wants to do
action = input("What do you want to do (add, get)? ")

#Memo creation function
def add_memo(text):
    query = (f"INSERT INTO memo (text) VALUES('{text}')") 
    cursor.execute(query)
    db.commit()
    memo_id = cursor.lastrowid
    print(f"Created memo : {memo_id}")

def get_memo():
    query = (f"SELECT * FROM memo")
    cursor.execute(query)
    result = cursor.fetchall()

    for memo in result:
        print(memo)

#Run any of the functions depending on the input
if(action == "add"):
    memo_text = input("Enter new memo : ") #Get the memo from the CLI
    add_memo(f"{memo_text}") #Create the memo

if(action == "get"):
    get_memo()