from json import dumps
import allure
import pytest
import requests
from assertpy.assertpy import assert_that
from config import Data
from services.base_client import BaseClient
from utils.read_file import reader


@allure.title("Obtener todas las reservas")
@allure.link("FiveStarsCarService")
@allure.label("critical")
@pytest.mark.smoke
def test_get_all_bookings():
    response = requests.get(Data.BASE_URI, timeout=10)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


@allure.title("Obtener una reserva en Miami")
@allure.link("FiveStarsCarService")
@allure.label("critical")
def test_get_a_booking():
    response = requests.post(Data.BASE_URI, timeout=10).json()
    drop_off_location = [booking['drop_off_location'] for booking in response]
    assert_that(drop_off_location).contains('Miami')


@allure.title("Crear una reserva nueva")
@allure.link("FiveStarsCarService")
@allure.label("critical")
def test_create_booking():
    payload = dumps(reader('booking.json'))
    response = requests.post(Data.BASE_URI, data=payload, headers=BaseClient, timeout=10)
    assert_that(response.status_code).is_equal_to(requests.codes.created)
