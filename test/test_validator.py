import unittest
import requests


class test_validator(unittest.TestCase):  
    
    def test_connection_tx(self, state = 'tx'):
        url = f"https://covidtracking.com/api/v1/states/{state}/daily.json"
        COVID_Data = requests.get(url = url)
        self.assertEqual(COVID_Data.status_code, 200)
        


