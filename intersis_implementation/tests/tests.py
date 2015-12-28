from django.test import TestCase


class DummyTests(TestCase):
    def test_should_pass(self):
        self.assertTrue(True)

    def test_should_fail(self):
        self.assertTrue(False)
