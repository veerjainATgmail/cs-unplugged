from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.TrainStationsResourceGenerator import TrainStationsResourceGenerator


@tag("resource")
class TrainStationsResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_subtitle_circular_a4(self):
        query = QueryDict("tracks=circular&paper_size=a4")
        generator = TrainStationsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "circular tracks - a4"
        )

    def test_subtitle_circular_letter(self):
        query = QueryDict("tracks=circular&paper_size=letter")
        generator = TrainStationsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "circular tracks - letter"
        )

    def test_subtitle_twisted_a4(self):
        query = QueryDict("tracks=twisted&paper_size=a4")
        generator = TrainStationsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "twisted tracks - a4"
        )

    def test_subtitle_twisted_letter(self):
        query = QueryDict("tracks=twisted&paper_size=letter")
        generator = TrainStationsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "twisted tracks - letter"
        )