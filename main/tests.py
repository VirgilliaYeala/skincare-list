from django.test import TestCase, Client
from main.models import Product

class mainTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(brand = "brand", name="nama", amount=2, description="test", price ="Rupiah")

    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def test_brand_product(self):
        buku = Product.objects.get(id=1)
        field_label = buku._meta.get_field('brand').verbose_name
        self.assertEqual(field_label, 'brand')

    def test_name_product(self):
        buku = Product.objects.get(id=1)
        field_label = buku._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_product(self):
        buku = Product.objects.get(id=1)
        field_label = buku._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')
    
    def test_amount_product(self):
        buku = Product.objects.get(id=1)
        field_label = buku._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')

    def test_price_product(self):
        buku = Product.objects.get(id=1)
        field_label = buku._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')