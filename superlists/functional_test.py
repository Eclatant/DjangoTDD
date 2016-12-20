from selenium import webdriver
import unittest


class SomeTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)

        self.fail('Finished the test!')

if __name__=='__main__':
    unittest.main(warnings='ignore')

browser = webdriver.Chrome('chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
