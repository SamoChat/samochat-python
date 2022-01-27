import requests
import samochat

class OAuthHandler:


    # gets the access token
    def get_api_token():

        url = 'https://samochat.eu.auth0.com/oauth/token'
      
        data = "{\"client_id\":\""+ samochat.client_id +"\",\"client_secret\":\""+ samochat.client_secret +"\",\"audience\":\"https://api.samochat.net\",\"grant_type\":\"client_credentials\"}"
        headers = { 'content-type': "application/json" }

        request = requests.post(url, data=data, headers=headers) # sends the request, the headers and the content 

        data = request.json()

        api_key = data['access_token'] 
    
        return api_key


