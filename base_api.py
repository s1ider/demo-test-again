import unittest
import requests
import yaml
import xmltodict


class BaseApiTest(unittest.TestCase):
    def setUp(self):
        self.settings = yaml.load(open('settings.yml'))
        self.base_url = self.settings['base_url']

        self.login()

    def login(self):
        url = self.base_url + '/user/login'

        params = {
            'login': self.settings['credentials']['login'],
            'password': self.settings['credentials']['password']
        }

        r = requests.post(url, data=params)
        self.cookies = r.cookies

    def create_issue(self):
        """ Creates test issue and returns issue_id """
        url = self.base_url + '/issue'
        params = {
            'project': 'API',
            'summary': 'Test issue from helper - DZ',
            'description': 'Credsafassdfa'
        }

        r = requests.put(url, data=params, cookies=self.cookies)
        self.assertEqual(r.status_code, 201)

        issue_id = r.headers['Location'].split('/')[-1]
        return issue_id

