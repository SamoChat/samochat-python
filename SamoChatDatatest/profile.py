from SamoChat.auth import OAuthHandler
import SamoChat
import requests
from SamoChat import SamoChatData

class Profile:

    
    # fetches the details of a profile
    def get_profile(username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(SamoChat._base_url + "profile/" + username, headers=headers) # sends the get requests to the api with the needed headers
            profile_data = response.json() # gets the json out of the response

        # catches any content decoding errors
        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        # catches any connection errors
        except requests.exceptions.ConnectionError:
            return "Connection refused"
         
        return profile_data