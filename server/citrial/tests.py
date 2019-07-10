from unittest import TestCase


class TestPractice(TestCase):
    def testGood(self):
        self.assertEqual(1, 1)

    def testBad(self):
        self.assertEqual(1, 0)


def test_pytest_testfinder():
    from citrial.models import foo
    foo()
    assert 1 == 0
