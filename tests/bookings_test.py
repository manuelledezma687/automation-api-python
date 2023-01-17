import requests
from assertpy.assertpy import assert_that
from json import dumps

from config import BASE_URI
from services.BaseClient import BaseClient
from utils.read_file import reader
from utils.request import APIRequest
from services.assertions import Assertions

def test_get_all_bookings():
    response = APIRequest.get(BASE_URI)
    Assertions.get_status_ok(response)
    
def test_get_a_booking():
    response = APIRequest.get(BASE_URI).json()
    drop_off_location = [booking['drop_off_location'] for booking in response]
    Assertions.get_contains_word(drop_off_location,"Miami")

def test_create_booking():
    payload = dumps(reader('booking.json'))
    response = APIRequest.post(BASE_URI,payload, BaseClient)
    Assertions.get_status_created(response)