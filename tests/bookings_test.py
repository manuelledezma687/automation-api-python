import allure
import pytest
from json import dumps

from config import BASE_URI
from services.BaseClient import BaseClient
from utils.read_file import reader
from utils.request import APIRequest
from services.assertions import Assertions

@allure.title("Obtener todas las reservas")
@allure.link("FiveStarsCarService")
@allure.label("critical")
@pytest.mark.smoke
def test_get_all_bookings():
    response = APIRequest.get(BASE_URI)
    Assertions.get_status_ok(response)

@allure.title("Obtener una reserva en Miami")
@allure.link("FiveStarsCarService")
@allure.label("critical")
def test_get_a_booking():
    response = APIRequest.get(BASE_URI).json()
    drop_off_location = [booking['drop_off_location'] for booking in response]
    Assertions.get_contains_word(drop_off_location,"Miami")

@allure.title("Crear una reserva nueva")
@allure.link("FiveStarsCarService")
@allure.label("critical")
def test_create_booking():
    payload = dumps(reader('booking.json'))
    response = APIRequest.post(BASE_URI,payload, BaseClient)
    Assertions.get_status_created(response)