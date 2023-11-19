import reflex as rx

accent_color = "#ff6f00"

default_styles = {
    "::selection": {
        "background": accent_color,
    },
    rx.Input: {
        "border": "1px solid #ccc",
        "border-radius": "0.25rem",
        "padding": "0.25rem",
        "margin": "0.5rem",
        "width": "75%",
        "height": "2rem",
        "outline": "none",
        "font-size": "1rem",
        "transition": "border-color 0.2s ease-in-out",
    },
    rx.Password: {
        "border": "1px solid #ccc",
        "border-radius": "0.25rem",
        "padding": "0.25rem",
        "margin": "0.5rem",
        "width": "75%",
        "height": "2rem",
        "outline": "none",
        "font-size": "1rem",
        "transition": "border-color 0.2s ease-in-out",
        "placeholder": "Password",
    },
}