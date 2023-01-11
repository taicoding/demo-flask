from flask_testing import TestCase
from flask import current_app, url_for
from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        return app

    def test_app_exist(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config["TESTING"])

    def test_index_redirect(self):
        response = self.client.get(url_for("index"))
        print(response.location)
        self.assertRedirects(response, url_for("doxeando_ips"))

    def test_hello_get(self):
        response = self.client.get(
            url_for(
                "doxeando_ips",
            )
        )
        self.assert200(response)

    def test_hello_post(self):
        fake_form = {
            "username": "fake-username",
            "password": "fake-password",
        }

        response = self.client.post(
            url_for("doxeando_ips"),
            data=fake_form,
        )
        # print(response.location)
        self.assertRedirects(response, url_for("index"))
