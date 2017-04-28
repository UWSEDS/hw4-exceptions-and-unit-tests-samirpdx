import unittest
from data_action import get_data
from data_action import delete_data

test_url_1 = "https://data.seattle.gov/resource/4xy5-26gy.csv"
test_url_2 = "https://data.seattle.gov/resource/4xy5-27gy.csv"


class TestDataAction(unittest.TestCase):

# Test get_data function

    def testGetData(self):
        
        test_url_1 = "https://data.seattle.gov/resource/4xy5-26gy.csv"
        test_url_2 = "https://data.seattle.gov/resource/4xy5-27gy.csv"
        delete_data(test_url_1)

        # Test 1:  URL points to a file that does exist, thus download should occur.
        result = get_data(test_url_1)
        self.assertTrue(result == "Download performed successfully.")

        # Test 2:  URL was already downloaded locally.
        result = get_data(test_url_1)
        self.assertTrue(result == "File exists locally, skipping download.")

        # Test 3:  URL points to a file that does not exist.
        result = get_data(test_url_2)
        self.assertTrue(result == "URL does not point to a file that exists.")


# Test delete_data function
    def testDeleteData(self):

        test_url_1 = "https://data.seattle.gov/resource/4xy5-26gy.csv"
        test_url_2 = "https://data.seattle.gov/resource/4xy5-27gy.csv"
        delete_data(test_url_1)
        get_data(test_url_1)

        # Test 1:  URL delete is successful
        result = delete_data(test_url_1)
        self.assertTrue(result == "File successfully removed locally.")

        # Test 2:  URL not found locally.  File from URL is valid.
        result = delete_data(test_url_1)
        self.assertTrue(result == "File from URL not found locally.")



if __name__ == '__main__':
    unittest.main()
