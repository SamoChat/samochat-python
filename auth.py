import requests
import samochat

class OAuthHandler:

    #clientID = None
    #clientSecret = None

    # gets the access token
    def get_api_token():
        # the OAuth url for authentication
        url = 'https://samochat.eu.auth0.com/oauth/token'
        # the data authorization data that will be sent to the OAuth url
        data = "{\"client_id\":\""+ samochat.client_id +"\",\"client_secret\":\""+ samochat.client_secret +"\",\"audience\":\"https://api.samochat.net\",\"grant_type\":\"client_credentials\"}"
        headers = { 'content-type': "application/json" }

        # sends the post request
        request = requests.post(url, data=data, headers=headers) # sends the request, the headers and the content 

        # fetches the json request of the request
        data = request.json()

        # loads the 'access_token' json node into a variable
        api_key = data['access_token'] 
    
        return api_key


