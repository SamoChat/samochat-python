from samochat import OAuthHandler
import samochat
import requests

class SamochatData:

     # Gets the details of the specified profile in json format
    def get_profile(self, username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(samochat._base_url + "profile/" + username, headers=headers)
            profile_data_node = response.json() 
  
        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        except requests.exceptions.ConnectionError:
            return "Connection refused"
         
        return profile_data_node

    # fetches the public posts of the specified profile
    def get_posts(self, username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(samochat._base_url + "profile/" + username + "/timeline", headers=headers) 
            posts_data_node = response.json() 
    

        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        except requests.exceptions.ConnectionError:
            return  "Connection refused"
         
        return posts_data_node

    # fetches the name of the specified profile
    def get_name(self, username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(samochat.__base_url__ + "user/" + username + "?query=name", headers=headers)
            output_json = response.json() 
            name_node = output_json['name']
    

        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        except requests.exceptions.ConnectionError:
            return  "Connection refused"
         
        return name_node

    # fetches the age of the specified profile
    def get_age(self, username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(samochat.__base_url__ + "user/" + username + "?query=age", headers=headers)
            output_json = response.json()
            age_node = output_json['age']
    
        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        except requests.exceptions.ConnectionError:
            return  "Connection refused"
         
        return age_node

    # fetches the gender of the specified profile
    def get_gender(self, username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(samochat.__base_url__ + "user/" + username + "?query=gender", headers=headers) 
            output = response.json() 
            gender = output['gender']
    
        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        except requests.exceptions.ConnectionError:
            return  "Connection refused"
         
        return gender

    # fetches the location of the specified user
    def get_location(self, username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(samochat.__base_url__ + "user/" + username + "?query=location", headers=headers) 
            output_json = response.json() 
            location_node = output_json['location']
    
        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        except requests.exceptions.ConnectionError:
            return  "Connection refused"
         
        return location_node    

    # fetches the amount of SamoCredits the specified user has got
    def get_samocredits(self, username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(samochat.__base_url__ + "user/" + username + "?query=samocredits", headers=headers) 
            output_json = response.json()
            samocredits_node = output_json['SamoCredits']
    
        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        except requests.exceptions.ConnectionError:
            return  "Connection refused"
         
        return samocredits_node

    # fetches when the specified user joined SamoChat 
    def get_rank(self, username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(samochat.__base_url__ + "user/" + username + "?query=rank", headers=headers)
            output_json = response.json()
            rank_node = output_json['rank']
    
        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        except requests.exceptions.ConnectionError:
            return  "Connection refused"
         
        return rank_node 

    # fetches the number of public videos the specified user has uploaded
    def get_videos(self, username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(samochat.__base_url__ + "user/" + username + "?query=videos", headers=headers)
            output_json = response.json()
            videos_node = output_json['videos']
    
        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        except requests.exceptions.ConnectionError:
            return  "Connection refused"
         
        return videos_node 

     # fetches the number of public photos the specified user has uploaded
    def get_photos(self, username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(samochat.__base_url__ + "user/" + username + "?query=photos", headers=headers) 
            output_json = response.json() 
            photos_node = output_json['photos']
    
        # catches any content decoding errors
        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        except requests.exceptions.ConnectionError:
            return  "Connection refused"
         
        return photos_node

    # fetches when the specified user joined SamoChat 
    def get_joined(self, username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(samochat.__base_url__ + "user/" + username + "?query=joined", headers=headers)  
            output_json = response.json()
            joined_node = output_json['joined']
    
        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        except requests.exceptions.ConnectionError:
            return  "Connection refused"
         
        return joined_node
        
    # fetches the about of the specified user
    def get_about(self, username):
        try:

            headers = { 'Authorization': "Bearer " + OAuthHandler.get_api_token() }
            response = requests.get(samochat.__base_url__ + "user/" + username + "?query=about", headers=headers) 
            output_json = response.json()
            about_node = output_json['about']
    
        except requests.exceptions.ContentDecodingError:
            return "Couldn't fetch data"
        except requests.exceptions.ConnectionError:
            return  "Connection refused"
         
        return about_node               
                        