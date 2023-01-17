from assertpy.assertpy import assert_that
import requests

class Assertions:
    
    def get_status_ok(response):
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
    
    def get_status_created(response):
        assert_that(response.status_code).is_equal_to(requests.codes.created)

    
    def get_contains_word(key,keyword):
        assert_that(key).contains(keyword)