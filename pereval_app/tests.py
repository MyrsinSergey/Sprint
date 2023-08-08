from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Users, PerevalAdded, Coords, Level, Images
from .serializers import PerevalSerializer, DetailedPerevalSerializer
from rest_framework.renderers import JSONRenderer


"""Тест, проверяющий создание новых перевалов"""
class PerevalAddTests(APITestCase):
    def setUp(self) -> None:
        self.pereval_1 = PerevalAdded.objects.create(
            user=Users.objects.create(
                email="Test1@mail.ru",
                fam="Test1",
                name="Test1",
                otc="Test1",
                phone="+11111111111"
            ),
            beauty_title="Test1",
            title="Test1",
            other_titles="Test1",
            connect='',
            coords=Coords.objects.create(
                latitude=1.1,
                longitude=1.1,
                height=1
            ),
            level=Level.objects.create(
                winter='А1',
                summer='A1',
                autumn='А1',
                spring='А1'
            ),
            images=Images.objects.create(
                title_1='Image 1',
                image_1='image1.jpg',
                title_2='Image 2',
                image_2='image2.jpg',
                title_3='Image 3',
                image_3='image3.jpg'
            )
        )

        self.pereval_2 = PerevalAdded.objects.create(
            user=Users.objects.create(
                email="Test2@mail.ru",
                fam="Test2",
                name="Test2",
                otc="Test2",
                phone="+22222222222"
            ),
            beauty_title="Test2",
            title="Test2",
            other_titles="Test2",
            connect='',
            coords=Coords.objects.create(
                latitude=2.2,
                longitude=2.2,
                height=2),
            level=Level.objects.create(
                winter='',
                summer='',
                autumn='',
                spring=''
            ),
            images=Images.objects.create(
                title_1='',
                image_1='',
                title_2='',
                image_2='',
                title_3='',
                image_3=''
            )
        )

        self.pereval_3 = PerevalAdded.objects.create(
            user=Users.objects.create(
                email="Test3@mail.ru",
                fam="Test3",
                name="Test3",
                otc="Test3",
                phone="+33333333333"
            ),
            beauty_title="Test3",
            title="Test3",
            other_titles="Test3",
            connect='',
            coords=Coords.objects.create(
                latitude=3.3,
                longitude=3.3,
                height=3),
            level=Level.objects.create(
                winter='',
                summer='',
                autumn='',
                spring=''
            ),
            images=Images.objects.create(
                title_1='',
                image_1='',
                title_2='',
                image_2='',
                title_3='',
                image_3=''
            ),
            status='pending'
        )

    def test_get_list(self):
        url = reverse('submitData')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2, self.pereval_3], many=True).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 3)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())

    def test_get_detail(self):
        url = reverse('submitData_detail', args=(self.pereval_1.id,))
        response = self.client.get(url)
        serializer_data = DetailedPerevalSerializer(self.pereval_1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())


class PerevalSerializerTest(TestCase):
    def setUp(self) -> None:
        self.pereval_1 = PerevalAdded.objects.create(
            user=Users.objects.create(
                email="Test1@mail.ru",
                fam="Test1",
                name="Test1",
                otc="Test1",
                phone="+11111111111"
            ),
            beauty_title="Test1",
            title="Test1",
            other_titles="Test1",
            connect='',
            coords=Coords.objects.create(
                latitude=1.1,
                longitude=1.1,
                height=1
            ),
            level=Level.objects.create(
                winter='А1',
                summer='A1',
                autumn='А1',
                spring='А1'
            ),
            images=Images.objects.create(
                title_1='Image 1',
                image_1='image1.jpg',
                title_2='Image 2',
                image_2='image2.jpg',
                title_3='Image 3',
                image_3='image3.jpg'
            )
        )

    def test_check_pereval(self):
        serializer = PerevalSerializer(self.pereval_1)
        serialized_data = JSONRenderer().render(serializer.data)
        response = self.client.post(reverse('submitData'), serialized_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_id = response.data['id']
        response = self.client.get(reverse('submitData_detail', args=[new_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['beauty_title'], 'Test1')
        self.assertEqual(response.data['title'], 'Test1')
        self.assertEqual(response.data['other_titles'], 'Test1')

        user = response.data['user']
        self.assertEqual(user['email'], 'Test1@mail.ru')
        self.assertEqual(user['fam'], 'Test1')
        self.assertEqual(user['name'], 'Test1')
        self.assertEqual(user['otc'], 'Test1')
        self.assertEqual(user['phone'], '+11111111111')

        coords = response.data['coords']
        self.assertEqual(coords['latitude'], 1.1)
        self.assertEqual(coords['longitude'], 1.1)
        self.assertEqual(coords['height'], 1)

        level = response.data['level']
        self.assertEqual(level['winter'], 'А1')
        self.assertEqual(level['summer'], 'A1')
        self.assertEqual(level['autumn'], 'А1')
        self.assertEqual(level['spring'], 'А1')

        images = response.data['images']
        self.assertEqual(images['title_1'], 'Image 1')
        self.assertEqual(images['title_2'], 'Image 2')
        self.assertEqual(images['title_3'], 'Image 3')