import requests


# This should probably fail if you try to run it directly, because the service isn't running.
# Use the ./integration_tests.sh script.

# Assumes url_shortener service is running on localhost 8080

class TestURLShortener:

    @classmethod
    def setup_class(cls):
        # for the purposes of testing, need to delete DB
        # however the cocker dynamoDB container has no state, so no need to
        # delete
        pass

    def test_hello(self):
        r = requests.get('http://localhost:8080/hello')
        assert r.json()['success'] == 'hello'

    def test_get_index(self):
        r = requests.get('http://localhost:8080')
        assert b'Your Full URL' in r.content

    def test_post_URL_and_get_shortened_url(self):
        LONG_URL = "http://google.com"

        # verify index page
        r = requests.get('http://localhost:8080')
        assert b'Your Full URL' in r.content

        # make POST
        r = requests.post('http://localhost:8080/url', json={"url": LONG_URL})
        post_json = r.json()
        assert 'success' in post_json

        # GET shortened URL
        url = post_json['success']

        # GET the redirect
        r = requests.get('http://localhost:8080' + url, allow_redirects=False)
        assert r.status_code == 302
        assert r.headers['Location'] == LONG_URL

        # GET the url-info
        r = requests.get('http://localhost:8080/info' + url)

        assert r.json()['success']['long_url'] == LONG_URL
