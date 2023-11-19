"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from auth.styles import default_styles
from auth.state import FirebaseState, MainState

@rx.page("/login")
def login_page() -> rx.Component:
    return rx.container(
        rx.input(placeholder="Email", on_change=MainState.set_email),
        rx.password(placeholder="Password", on_change=MainState.set_password),
        rx.hstack(
            rx.button("Login", on_click=FirebaseState.login_user, is_loading=MainState.button_waiting),
            rx.button("Create account", on_click=rx.redirect("/create-account")),
        ),
        rx.cond(
            FirebaseState.something_went_wrong,
            rx.alert("Something went wrong. Please try again."),
        ),
        )

@rx.page("/create-account")
def create_account_page() -> rx.Component:
    return rx.container(
        rx.input(placeholder="Email", on_change=MainState.set_email),
        rx.password(placeholder="Password" , on_change=MainState.set_password),
        rx.password(placeholder="Confirm password", on_change=MainState.set_password_confirm),
        rx.button("Create account", on_click=FirebaseState.create_user, is_loading=MainState.button_waiting),
        )

@rx.page("/welcome", on_load = FirebaseState.require_login)
def welcome_page() -> rx.Component:
    return rx.text("You are logged in")

# Add state and pages to the app.
app = rx.App(style = default_styles)
app.compile()
