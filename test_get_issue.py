import unittest
import requests
import xmltodict


class TestGetIssue(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://codespace-api.myjetbrains.com/youtrack/rest'
        self.creds = ('root', 'c11desp@ce')

    def test_get_issue(self):
        issue_id = 'API-1'
        url = self.base_url + '/issue/' + issue_id
        response = requests.get(url, auth=self.creds)
        response_dict = xmltodict.parse(response.text)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_dict['issue']['@id'], issue_id)

    def test_get_not_existed_issue(self):
        url = self.base_url + '/issue/' + 'NOTEXISTED'

        r = requests.get(url, auth=self.creds)
        self.assertEqual(r.status_code, 404)


if __name__ == '__main__':
    unittest.main()

