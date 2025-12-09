from app.main import outdated_products
from unittest import mock
import datetime
import pytest


@pytest.fixture()
def mocked_function():
    with mock.patch("app.main.datetime") as mock_datetime:
        yield mock_datetime.date.today


@pytest.mark.parametrize(
    "prod, exp",
    [([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2026, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2026, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2025, 2, 1),
            "price": 160
        }
    ],
        ["duck"]
    )]
)
def test_outdated_products_works(
    prod: list,
    exp: list,
    mocked_function
) -> None:
    mocked_function.return_value = datetime.date.today()
    assert exp == outdated_products(prod)


def test_outdated_products_has_called(mocked_function) -> None:
    mocked_function.return_value = datetime.date.today()
    prod = [
        {
            "name": "duck",
            "expiration_date": datetime.date(2025, 2, 1),
            "price": 160
        }
    ]
    outdated_products(prod)
    mocked_function.assert_called_once()
