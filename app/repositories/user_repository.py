from bson import ObjectId

class UserRepository:
    def __init__(self, db):
        self.collection = db['users_collection']

    def email_exists(self, email: str) -> bool:
        return bool(self.collection.find_one({'email': email}))

    def create_user(self, user_data: dict) -> str:
        result = self.collection.insert_one(user_data)
        return str(result.inserted_id)