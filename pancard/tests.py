import unittest
from django.test import TestCase, Client
import os
from PIL import Image
import io


class TestPancardActions(unittest.TestCase):
    """
    Test case for pancard upload
    """
    def setUp(self):
        self.client = Client()

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file
    
    def test_upload_file(self):
        """
        Upload file success test
        """
        c = Client()
        pwd = os.path.dirname(__file__)
        photo_file = self.generate_photo_file()

        data = {
                'file':photo_file,
                'name':"test"
        }
        response = c.post('/pancard/',data, format='multipart')
        self.assertEqual(response.status_code, 200)


