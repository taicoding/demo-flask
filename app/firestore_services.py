import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'flask-platzi-374905'
credentials = credentials.Certificate('./secret/flask-platzi-374905-firebase-adminsdk-uo90w-9ed3aaa5b7.json')
firebase_admin.initialize_app(credentials,{'projectId':project_id})

db = firestore.client()

def get_users():
    return db.collection("users").get()

def get_todos(user_id):
    return db.collection("users").document(user_id).collection("todos").get()