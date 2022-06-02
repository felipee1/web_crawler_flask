import sys
sys.path.insert(1, '/app/app')
from app import app
import unittest

class FlasTest(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_failed_scrape(self):
        tester = app.test_client(self)
        response = tester.post("/scrape")
        status_code = response.status_code
        self.assertEqual(status_code, 412)
    
    def test_success_scrape(self):
        tester = app.test_client(self)
        response = tester.post("/scrape", data={"url":"http://localhost:5000/"})
        status_code = response.status_code
        self.assertEqual(status_code, 200)
    
    def test_success_list(self):
        tester = app.test_client(self)
        response = tester.post("/list")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

if __name__ == "__main__":
    unittest.main()