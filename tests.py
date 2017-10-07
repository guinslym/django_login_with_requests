import unittest
from scrap import *

class TestAccessingAuthPage(unittest.TestCase):

    def test_main_return_a_title(self):
        title = main()
        self.assertEqual(
            'Site administration',
            title,
            'Should have received Site administration as the title'
            )

if __name__ == '__main__':
    unittest.main()
