import requests
from django.contrib.auth.models import User
from django.test import TestCase
from shop.models import Director, Shop, Consultant
# Create your tests here.


class ModelsTestCase(TestCase):

    def setUp(self):
        # For 1 director
        user_id = User.objects.create_user(username="Saple_user", email="sample@gmail.com", password="test_test")
        director1 = Director.objects.create(user_id=user_id, name="Sample Boss")
        shop1_1 = Shop.objects.create(director=director1, shop_title="Perfect_Shop")
        shop1_2 = Shop.objects.create(director=director1, shop_title="Perfect_Shop2")
        consultant_for_shop1_1 = Consultant.objects.create(shop=shop1_1, name="Alex", sold_goods=5)
        consultant_for_shop1_2 = Consultant.objects.create(shop=shop1_2, name="Tom", sold_goods=8)

        # For 2 director
        user_id2 = User.objects.create_user(username="Saple_user2", email="sample2@gmail.com", password="test_test2")
        director2 = Director.objects.create(user_id=user_id2, name="Little Boss")
        shop2_1 = Shop.objects.create(director=director2, shop_title="Normal_Shop")
        shop2_2 = Shop.objects.create(director=director2, shop_title="Normal_Shop2")
        consultant_for_shop2_1 = Consultant.objects.create(shop=shop2_1, name="Ben", sold_goods=4)
        consultant_for_shop2_2 = Consultant.objects.create(shop=shop2_2, name="Ann", sold_goods=3)

    def test_relationship(self):
        director1 = Director.objects.get(name="Sample Boss")
        shop1_1 = Shop.objects.get(director=director1, shop_title="Perfect_Shop")
        consultant_for_shop1_1 = Consultant.objects.get(name="Alex")

        self.assertEqual(consultant_for_shop1_1.shop, shop1_1)
        self.assertEqual(shop1_1.director, director1)

        shop2_1 = Shop.objects.get(shop_title='Normal_Shop')
        self.assertNotEqual(shop2_1.director, director1)

        consultant_for_shop2_2 = Consultant.objects.get(name="Ann")
        self.assertNotEqual(consultant_for_shop1_1.shop, consultant_for_shop2_2.shop)


class ApiTestCase(TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api_methods/'

    def test_success_response(self):

        shop_info_api = self.base_url + 'shop/'
        response = requests.get(shop_info_api)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.text, None)

        director_info_api = self.base_url + 'director/'
        response = requests.get(director_info_api)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.text, None)
