import unittest
import requests
import yaml


class TestCreateIssue(unittest.TestCase):

    def setUp(self):
        settings = yaml.load(open('settings.yml'))
        self.base_url = settings['base_url']
        login = settings['credentials']['login']
        password = settings['credentials']['password']
        self.creds = (login, password)

    def test_create_issue(self):
        url = self.base_url + '/issue'
        params = {
            'project': 'API',
            'summary': 'Awesome summary - DZ',
            'description': 'Credsafasf'
        }

        r = requests.put(url, data=params, auth=self.creds)
        location = r.headers['Location']
        self.assertEqual(r.status_code, 200)

        r = requests.get(location, auth=self.creds)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__'
    unittest.main()
