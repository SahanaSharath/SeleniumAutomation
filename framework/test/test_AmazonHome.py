from SeleniumAutomation.framework.pom.AmazonHome import AmazonHome
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_AmazonHome(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.ah = AmazonHome(self.driver)

    @pytest.mark.run(order=1)
    def test_search(self):
        self.ah.searchProduct()
        self.ah.filter()
        # self.ah.clickSearch()

    
