import os
import json
import requests
from loguru import logger

import reflex as rx
import firebase_admin
from firebase_admin import auth
from dotenv import load_dotenv

load_dotenv()
firebase_admin.initialize_app()

class MainState(rx.State):
    pass

class MainState(MainState):
    email: str = ""
    password: str = ""
    password_confirm: str = ""
    user_infos: dict = {}

    button_waiting: bool = False
    create_user_button_waiting: bool = False
    something_went_wrong: bool = False


class FirebaseState(MainState):
    id_token: str = ""

    def reset_something_went_wrong(self):
        self.something_went_wrong = False

    def get_uid(self):
        return auth.verify_id_token(self.id_token).get('uid')

    def create_user(self):
        self.reset_something_went_wrong()
        self.button_waiting = True; yield
        if self.password != self.password_confirm:
            logger.debug("Passwords don't match")
            self.something_went_wrong = True
            return
        self.uid = auth.create_user(
            email=self.email,
            email_verified=False,
            password=self.password).uid
        self.button_waiting = False
        return rx.redirect("login")

    def login_user(self):
        load_dotenv()
        self.reset_something_went_wrong()
        self.button_waiting = True; yield
        request_ref = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={0}".format(os.getenv('WEB_API_KEY'))
        headers = {"content-type": "application/json; charset=UTF-8"}
        data = json.dumps({"email": self.email, "password": self.password, "returnSecureToken": True})
        request_object = requests.post(request_ref, headers=headers, data=data)
        response = request_object.json()
        self.button_waiting = False
        if 'idToken' in response:
            logger.info(f"logged in as {response}")
            self.id_token = response['idToken']
            logger.info(f"logged in with id token {self.id_token}")
            return rx.redirect("/welcome")
        else:
            logger.debug(f"Something went wrong in login. Response: {response}")
            self.something_went_wrong = True


    def require_login(self, ) -> rx.Component:
        try:
            self.get_uid()
        except:
            logger.debug("User is not logged in. Redicting to '/login'")
            return rx.redirect("login/")