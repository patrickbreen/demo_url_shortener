
import app
import requests


# assume url_shortener service is running on localhost 8080


class TestURLShortener:

    @classmethod
    def setup_class(cls):
        # for the purposes of testing, need to delete DB
        # however the cocker dynamoDB container has no state, so no need to delete
        pass

    def test_hello(self):
        r = requests.get('http://localhost:8080/hello')
        assert r.json()['success'] == 'hello'



    def test_get_index(self):
        r = requests.get('http://localhost:8080')
        assert b'Your Full URL' in r.content



    def test_post_URL_and_get_shortened_url(self):
        # TODO

        # make POST

        # GET shortened URL

        # GET the redirect


        # GET the url-info

        r = requests.get('http://localhost:8080')
        assert b'Your Full URL' in r.content