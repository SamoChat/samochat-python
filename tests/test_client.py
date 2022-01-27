import unittest
import os
import samochat
from samochat import SamochatData

class TestSamoChatData(unittest.TestCase):

    samochat.client_id = str(os.getenv('client_id'))
    samochat.client_secret = str(os.getenv('client_secret'))
    
    def test_get_name(self):
         data = SamochatData()
         # checks whether the outputs are equal
         self.assertEqual(data.get_name("SamoChat"), "SamoChat")
            
    def test_get_age(self):
         data = SamochatData()
         self.assertEqual(data.get_age("Samochat"), " 14 years ")

    def test_get_gender(self):
         data = SamochatData()
         self.assertEqual(data.get_gender("Samochat"), "Male")

    def test_get_location(self):
         data = SamochatData()
         self.assertEqual(data.get_location("Samochat"), "Søborg, Danmark")
         
    def test_get_samocredits(self):
         data = SamochatData()
         self.assertEqual(data.get_samocredits("Samochat"), "100.000.349")   
         
    def test_get_rank(self):
         data = SamochatData()
         self.assertEqual(data.get_rank("Samochat"), "Elite")

    def test_get_videos(self):
         data = SamochatData()
         self.assertEqual(data.get_videos("Samochat"), "1")

    def test_get_photos(self):
         data = SamochatData()
         self.assertEqual(data.get_photos("Samochat"), "31")

    def test_get_joined(self):
         data = SamochatData()
         self.assertEqual(data.get_joined("Samochat"), "   Member since 3 years ago  ")

    def test_get_about(self):
         data = SamochatData()
         self.assertEqual(data.get_about("Samochat"), " What's your idea?: To connect everyone, everywhere in a 💯 % secure and private way  About Me: We are the first Social media to truly respect and guard your privacy. Made in  but based in 🇩🇰  Website: Samochat.net ")                                   

if __name__ == '__main__':
    unittest.main()