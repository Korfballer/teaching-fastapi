"""The Restaurant application."""

# Standard library imports
# n/a

# Third party imports
from fastapi import FastAPI

# Local application imports
from .models import Order, Seats


# Create an application
the_app = FastAPI()


# Define a trivial restauraunt menu
menu = {
    "Starters": {
        "Olives": 4,
        "Bread": 3,
    },
    "Mains": {
        "Margherita": 10,
        "Spaghetti Bolognese": 8,
        "Salmon": 15,
    },
    "Desserts": {
        "Chocolate cake": 5,
        "Waffles And Ice-cream": 4,
    },
    "Drinks": {
        "Tap Water": 0,
        "Sparkling Water": 1,
        "Lemonade": 4,
    }
}


@the_app.get("/")
def welcome() -> dict:
    """Welcome.

    Returns:
        dict: Welcome message
    """
    return {"message": "Welcome to our restaurant"}


@the_app.post("/waiter")
def find_any_waiter() -> dict:
    """Speak to the waiter.

    Returns:
        dict: Waiter greeting
    """
    return {"message": "Hello, I'm your waiter for today."}


@the_app.post("/waiter/{name}")
def find_waiter(name: str) -> dict:
    """Speak to a specific waiter.

    Args:
        name (str): Name of waiter

    Returns:
        dict: Waiter greeting
    """
    return {"message": f"Hello, I'm {name.title()}, your waiter for today."}


@the_app.post("/table")
def find_table(seats: Seats) -> dict:
    """Ask for a table with a given number of seats.

    Args:
        seats (Seats): Number of seats required

    Returns:
        dict: Table number
    """
    n_seats = seats.seats

    output = {"Table number": 100 + n_seats}

    return output


@the_app.get("/menu")
def get_menu() -> dict:
    """Get menu.

    Returns:
        dict: Menu
    """
    return menu


@the_app.post("/order")
def post_order(order: Order) -> dict:
    """Order item(s) from the menu.

    Args:
        order (Order): Food and/or drink orders.

    Returns:
        dict: Order confirmation
    """
    food = order.food
    drinks = order.drinks

    return {
        "Food in its way": food,
        "Drinks on their way": drinks,
    }


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(the_app, host="127.0.0.1", port=8000)
