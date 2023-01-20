import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'flask-platzi-374905'
credentials = credentials.Certificate('key.json')
firebase_admin.initialize_app(credentials,{'projectId':project_id})

db = firestore.client()

def get_users():
    return db.collection("users").get()

def get_user(user_id):
    return db.collection("users").document(user_id).get()

def get_todos(user_id):
    return db.collection("users").document(user_id).collection("todos").get()

def user_put(user_data):
    user_ref = db.collection("users").document(user_data.username)
    user_ref.set({"password":user_data.password})
    
def get_todos(user_id):
    return db.collection("users").document(user_id).collection("todos").get()

def put_todos(user_id, descripcion):
    todos_collection_ref = db.collection("users").document(user_id).collection("todos")
    todos_collection_ref.add({"descripcion":descripcion, "done":False})
    
def delete_todo(user_id, todo_id):
    todos_ref = _get_todo_ref(user_id, todo_id)
    todos_ref.delete()

def update_todo(user_id, todo_id,done):
    todo_done = not bool(done)
    todos_ref = _get_todo_ref(user_id, todo_id)
    todos_ref.update({"done":not done})


def _get_todo_ref(user_id, todo_id):
    return db.document("users/{}/todos/{}".format(user_id, todo_id))