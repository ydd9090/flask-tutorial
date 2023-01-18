import unittest

from app import app,db
from app.models import Movie,User

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI="sqlite:///:memory:"
        )
        db.create_all()
        user = User(name="Test",username="test")
        user.set_password("12345")
        movie = Movie(title="Test Movie Title",year="2019")
        db.session.add_all([user,movie])
        db.session.commit()
        self.client = app.test_client()
        self.runner = app.test_cli_runner()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_app_exist(self):
        self.assertIsNotNone(app)

    def test_app_is_testing(self):
        self.assertTrue(app.config["TESTING"])


    def test_404_page(self):
        response = self.client.get("/nothing")
        data = response.get_data(as_text=True)
        self.assertIn("Page Not Found - 404",data)
        self.assertIn("Go Back",data)
        self.assertEqual(response.status_code,404)

    def test_index_page(self):
        response = self.client.get("/")
        data = response.get_data(as_text=True)
        self.assertIn("Test的观影清单",data)
        self.assertIn("Test Movie Title",data)
        self.assertEqual(response.status_code,200)

    def login(self):
        self.client.post("/login",data=dict(
            username="test",
            password="123"
        ),follow_redirects=True)

    def test_create_item(self):
        self.login()
        response =self.client.post("/",data=dict(
            title="New Movie",
            year="2019"
        ),follow_redirects=True)
        data = response.get_data(as_text=True)

        self.assertIn("Item created",data)
        self.assertIn("New Movie",data)