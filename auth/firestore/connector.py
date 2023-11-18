import firebase_admin
from firebase_admin import firestore
import bcrypt

from auth.firestore.errors import UserAlreadyExistsError


class FirebaseConnector:

    def __init__(self) -> None:
        self.db = firestore.client() # need to call initialize() first

    def create_user(self, user_id, password):
        if not self.__user_exists(user_id):
            password_hash = self.__hash_password(password)
            user_ref = self.db.collection(u'users').document(user_id)
            user_ref.set({
                u'password_hash': password_hash
            })
        else:
            raise UserAlreadyExistsError("User already exists")

    def login_user(self, username: str, password: str) -> bool:
        user_ref = self.db.collection(u'users').document(username)
        if user_ref.get().exists:
            stored_hash = user_ref.get().to_dict()['password_hash']
            return self.__check_password(password, stored_hash)
        else:
            return False

    def __user_exists(self, username: str):
        user_ref = self.db.collection(u'users').document(username)
        return user_ref.get().exists

    @staticmethod
    def __hash_password(password: str):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    @staticmethod
    def __check_password(password: str, hashed_password: str):
        return bcrypt.checkpw(password.encode(), hashed_password)

    @staticmethod
    def initialize():
        firebase_admin.initialize_app()


# # 
# username = "TomDDD"
# password = "12248942abF"

# FirebaseConnector.initialize()
# firestore_client = FirebaseConnector()
# firestore_client.create_user(username, password)