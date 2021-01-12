import unittest
import time
from selenium import webdriver
class Denglu(unittest.TestCase):

    def setUp(self):
        self.we = webdriver.Firefox()
        self.we.get("http://123.57.140.190/manage")
        time.sleep(5)
    def tearDown(self):
        self.we.close()
        self.we.quit()
    def test_denglu(self):
        self.we.find_element_by_name("Username").send_keys("admin")
        self.we.find_element_by_name("Password").send_keys("admin999")
        self.we.find_element_by_name("Submit").click()
        time.sleep(5)
        duanyan=self.we.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").text
        self.assertEqual(duanyan,"产品管理",msg="出现错误")

if __name__ == '__main__':
    unittest.main()