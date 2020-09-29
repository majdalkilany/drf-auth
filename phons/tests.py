from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Phons
# Create your tests here.

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()

        test_phons = Phons.objects.create(
            admin_name = test_user ,
            title_model = 'Samsung Galaxy A72' ,
            price = '$ 290' ,
            Processor = 'Unknown' ,
            RAM = ' 6 GB, 8 GB' ,
            Storage = '128 GB' ,
            Display = '6.7 inches' ,
            Camera = 'Penta Camera' 

        )

        test_phons.save() # Save the object to mock Database

    def test_phons_content(self):
        phons = Phons.objects.get(id=1)
        actual_admin_name =  str(phons.admin_name)
        actual_title_model = str(phons.title_model)
        actual_Processor = str(phons.Processor)
        actual_price = str(phons.price)
        actual_RAM = str(phons.RAM)
        actual_Storage = str(phons.Storage)
        actual_Display = str(phons.Display)
        actual_Camera = str(phons.Camera)


        
        self.assertEqual(actual_title_model, 'Samsung Galaxy A72')
        self.assertEqual(actual_price, '$ 290')
        self.assertEqual(actual_Processor, 'Unknown')
        self.assertEqual(actual_RAM, ' 6 GB, 8 GB')
        self.assertEqual(actual_Storage, '128 GB')
        self.assertEqual(actual_Display, '6.7 inches')
        self.assertEqual(actual_Camera, 'Penta Camera')
