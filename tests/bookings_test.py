import requests
from assertpy.assertpy import assert_that
from json import dumps

from config import BASE_URI
from utils.read_file import reader

def test_get_all_bookings():
    response = requests.get(BASE_URI)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    
def test_get_a_booking():
    response = requests.get(BASE_URI).json()
    drop_off_location = [booking['drop_off_location'] for booking in response]
    assert_that(drop_off_location).contains('Miami')

def test_create_booking():
    payload = dumps(reader('booking.json'))
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(BASE_URI,data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(requests.codes.created)