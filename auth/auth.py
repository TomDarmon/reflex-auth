"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from auth.state import State


def login_page() -> rx.Component:
    return rx.container(
        rx.input(placeholder="Username", on_change=State.set_username),
        rx.input(placeholder="Password", type="password", on_change=State.set_password),
        rx.button("Login", on_click=State.login_user, is_loading=State.loggin_button_waiting),
        rx.cond(
            State.logged_in,
            rx.button("Welcome", on_click=rx.redirect("/welcome")),
            rx.text("Wrong password"),
        ),
        )

def welcome_page() -> rx.Component:
    return rx.text("You are logged in")

# Add state and pages to the app.
app = rx.App()
app.add_page(login_page, route="/")
app.add_page(welcome_page, route="/welcome")
app.compile()
