import requests

class APIRequest:

    def get(url):
        response = requests.get(url)
        return response
    
    def post(url,payload, headers):
        response = requests.post(url, payload, headers)
        return response
    
    def put():
        pass
    
    def delete():
        pass