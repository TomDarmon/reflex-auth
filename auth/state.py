import reflex as rx
from auth.firestore.connector import FirebaseConnector
from auth.firestore.errors import UserAlreadyExistsError


class State(rx.State):
    FirebaseConnector.initialize()
    username: str = ""
    password: str = ""
    logged_in: bool = False
    wrong_password: bool = False


    # Animation
    loggin_button_waiting: bool = False
    create_user_button_waiting: bool = False

    def create_user(self):
        self.create_user_button_waiting = True
        if self.username == "" or self.password == "":
            return
        firestore_client = FirebaseConnector()
        try:
            firestore_client.create_user(self.username, self.password)
        except UserAlreadyExistsError:
            print("User already exists") # TO DO: Show user info
        self.create_user_button_waiting = False

    def login_user(self):
        self.loggin_button_waiting = True
        if self.username == "" or self.password == "":
            return

        yield
        firestore_client = FirebaseConnector()
        authentificated = firestore_client.login_user(self.username, self.password)
        if authentificated:
            self.wrong_password = False
            self.logged_in = True
        else:
            self.wrong_password = True
        self.loggin_button_waiting = False
