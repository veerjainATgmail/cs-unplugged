from tests.BaseTestWithDB import BaseTestWithDB
from classic.models import ClassicPage
from classic.management.commands._ClassicPagesLoader import ClassicPagesLoader
from utils.errors.CouldNotFindYAMLFileError import CouldNotFindYAMLFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.EmptyYAMLFileError import EmptyYAMLFileError


class ClassicPageLoaderTest(BaseTestWithDB):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loader_name = "classicpage"
        self.BASE_PATH = "tests/classic/loaders/assets/classicpages/"

    def test_basic_classic_page_loader_config(self):
        config_file = "basic-config.yaml"
        classic_page_loader = ClassicPagesLoader(
            structure_dir="",
            structure_filename=config_file,
            base_path=self.BASE_PATH,
        )
        classic_page_loader.load()
        pages = ClassicPage.objects.all()
        self.assertEqual(1, len(pages))
        self.assertQuerysetEqual(
            pages,
            ["<ClassicPage: Binary numbers>"]
        )

    def test_classic_page_loader_missing_configuration_file(self):
        config_file = "missing.yaml"
        classic_page_loader = ClassicPagesLoader(
            structure_dir="",
            structure_filename=config_file,
            base_path=self.BASE_PATH,
        )
        self.assertRaises(
            CouldNotFindYAMLFileError,
            classic_page_loader.load,
        )

    def test_classic_page_loader_empty_configuration_file(self):
        config_file = "empty.yaml"
        classic_page_loader = ClassicPagesLoader(
            structure_dir="",
            structure_filename=config_file,
            base_path=self.BASE_PATH,
        )
        self.assertRaises(
            EmptyYAMLFileError,
            classic_page_loader.load,
        )

    def test_classic_page_loader_missing_name_value(self):
        config_file = "missing-name.yaml"
        classic_page_loader = ClassicPagesLoader(
            structure_dir="",
            structure_filename=config_file,
            base_path=self.BASE_PATH,
        )
        self.assertRaises(
            MissingRequiredFieldError,
            classic_page_loader.load,
        )

    def test_classic_page_loader_multiple_configuration(self):
        config_file = "multiple.yaml"
        classic_page_loader = ClassicPagesLoader(
            structure_dir="",
            structure_filename=config_file,
            base_path=self.BASE_PATH,
        )
        classic_page_loader.load()
        pages = ClassicPage.objects.order_by("name")
        self.assertEqual(4, len(pages))
        self.assertQuerysetEqual(
            pages,
            [
                "<ClassicPage: Activities>",
                "<ClassicPage: Artificial intelligence>",
                "<ClassicPage: Binary numbers>",
                "<ClassicPage: CS Unplugged Book>",
            ],
        )
