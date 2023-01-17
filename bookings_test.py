import requests
from assertpy.assertpy import assert_that
from json import dumps

def test_get_all_bookings():
    response = requests.get('http://127.0.0.1:8000/bookings')
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    
def test_get_a_booking():
    response = requests.get('http://127.0.0.1:8000/bookings').json()
    drop_off_location = [booking['drop_off_location'] for booking in response]
    assert_that(drop_off_location).contains('Miami')

def test_create_booking():
    payload = dumps({
            "type_of_service": "hourly",
            "pick_up_location": "Atlanta Airport",
            "drop_off_location": "Miami",
            "flight_id": "MSE2123",
            "passengers": 3,
            "full_name": "Mike Adams",
            "email": "joseotero@gmail.com",
            "observations": "Hi, this is a comment.",
            "payment_method": "Cash",
            "date": "05/05/2022",
            "hour": "01:00",
            "referral": "MCLKD123",
            "created_at": "2023-01-13T09:02:47.068366",
            "status": 1
  }
)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post('http://127.0.0.1:8000/bookings',data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(requests.codes.created)