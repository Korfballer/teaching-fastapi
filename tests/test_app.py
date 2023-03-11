# Standard library imports
import json

# Third party imports
import pytest
import requests
from fastapi import Request
from fastapi.testclient import TestClient

# Local application imports
from app.main import the_app
from app.models import Order, Seats


# Add end-point for application for testing
@the_app.get("/client-info")
def get_client_info(request: Request):
    """
    Additional end-point to extract the URL that the application is running at.
    References:
        https://fastapi.tiangolo.com/advanced/using-request-directly/#use-the-request-object-directly
    """
    info = {
        "host": request.client.host,
        "port": request.client.port
    }

    return info

class Useful:
    """Useful fixtures."""

    @pytest.fixture
    def testclient(self):
        """Test client."""
        with TestClient(the_app) as client:

            yield client

    @pytest.fixture
    def url(self, testclient):
        """URL of the test client (to use for requests)."""
        response = testclient.get("/client-info").json()

        url = f"http://{response['host']}:{response['port']}"

        return url

    def test_root_via_requests(self, testclient):
        """Test welcome endpoint using requests."""
        # URL as defined in ./.vscode/launch.json, NOT app/main.py
        url = "http://127.0.0.1:8000"

        try:
            actual = requests.get(f"{url}").json()
        except requests.exceptions.ConnectionError:
            pytest.skip(
                "test_root_via_requests requires the application to be running"
                ". For Visual Studio Code users, use 'Run and Debug'")

        expected = {"message": "Welcome to our restaurant"}

        assert actual == expected


    def test_root_via_client(self, testclient):
        """Test welcome endpoint via the test client."""
        actual = testclient.get("/").json()

        expected = {"message": "Welcome to our restaurant"}

        assert actual == expected

@pytest.mark.usefixtures("testclient", "url")
class TestApp(Useful):
    """Test the application."""

    @pytest.mark.parametrize("name", [None, "Aaa", "bbb", "ccc"])
    def test_find_waiter(self, testclient, name):
        """Test waiter."""
        if name is None:
            expected_msg = "Hello, I'm your waiter for today."
            url = "/waiter"
        else:
            expected_msg = f"Hello, I'm {name.title()}, your waiter for today."
            url = f"/waiter/{name}"

        expected = {"message": expected_msg}

        actual = testclient.post(url).json()

        assert actual == expected

    @pytest.mark.parametrize("n_seats", [1, 3, 4])
    def test_find_table(self, testclient, n_seats):
        """Test the table endpoint."""
        data = Seats(seats=n_seats).to_dict()

        actual = testclient.post("/table", data=json.dumps(data)).json()

        expected = {"Table number": 100 + int(n_seats)}

        assert actual == expected

    @pytest.mark.parametrize("n_seats", [-2, 0, 0.9, 2.3])
    def test_find_table_error(self, testclient, n_seats):
        """Test the table endpoint with invalid inputs.

        Extended Summary:
            Check that an error is raised when requesting <1 seats.
        """
        with pytest.raises(ValueError):

            Seats(seats=n_seats).to_dict()


    @pytest.mark.parametrize("use_pydantic", [True, False])
    def test_order(self, testclient, use_pydantic):
        """Test the order endpoint."""

        if use_pydantic:
            order = Order(food="Salmon").to_dict()

        else:
            order = {"food": "Salmon"}
        actual = testclient.post("/order", data=json.dumps(order)).json()

        expected = {
            "Food in its way": "Salmon",
            "Drinks on their way": None,
        }

        assert actual == expected
