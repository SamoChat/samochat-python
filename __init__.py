
# importing the other classes allows the other files to use them while only calling the module itself instead of the file
# eg. instead of from SamoChat.client import SamoChatData we will do from SamoChat import  SamoChatData

# Authorization
from samochat.auth import OAuthHandler

# API data
from samochat.client import SamochatData

#from SamoChat.SamoChatData import *




# global variables
client_id = None
client_secret = None
__base_url__ = "https://api.samochat.net/"