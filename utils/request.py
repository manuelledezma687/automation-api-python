import requests
import allure

class APIRequest:

    @allure.step("Get")
    def get(url):
        response = requests.get(url)
        return response
    
    @allure.step("Post")
    def post(url,payload, headers):
        response = requests.post(url, payload, headers)
        return response
    
    @allure.step("Put")
    def put():
        pass
    
    @allure.step("Delete")
    def delete():
        pass