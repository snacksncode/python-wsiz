from mug import Mug
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mug = Mug("red", 10.0)

    def test_is_created(self):
        self.assertIsNotNone(self.mug)
        self.assertEqual(self.mug.get_content_amount(), 0.0)

    def test_can_fill_full(self):
        self.mug.fill("water", self.mug.capacity)

        self.assertEqual(self.mug.get_content_amount(), self.mug.capacity)
        self.assertEqual(self.mug.get_content_type(), "water")

    def test_pouring_out_everything_clears_up_content_type(self):
        self.mug.fill("water", self.mug.capacity)
        self.assertEqual(self.mug.get_content_type(), "water")

        self.mug.pour_out_liquid(self.mug.capacity)
        self.assertEqual(self.mug.get_content_type(), None)


if __name__ == "__main__":
    unittest.main()
