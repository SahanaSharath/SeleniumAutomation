from SeleniumAutomation.framework.base.Selenium_driver import SeleniumDriver
import time

class AmazonHome(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _searchBar = "twotabsearchtextbox"
    _toBeSearched = "watch"
    _searchClick = "nav-search-submit-text"
    _searchSymbol = "//input[@class='nav-input' and @value='Go']"
    _womenWatch = "//*[@id='leftNavContainer']/ul[1]/div/li[2]/span/ul/div/li[4]/span/a/span"
    _seeMoreBrands = "//*[@id='leftNavContainer']/ul[2]/li[2]/span/a/span"
    _selectBrand = "//h4[.='Brand']/following-sibling::ul/div/li[.='Fossil']//label"
    _verifyFilter = "//span[@id='s-result-count']/span/a[4]"
    _selectedBrand = "Fossil"


    def searchProduct(self):
        self.getElement(self._searchBar, "id")
        self.sendKeys(self._toBeSearched, self._searchBar)
        self.elementClick(self._searchSymbol, "xpath")
        return True

    # def clickSearch(self):
    #     self.elementClick(self._searchClick, "id")
    #     return True

    def filter(self):
        self.waitForElement(self._womenWatch,"xpath",20,0.5)
        self.elementClick(self._womenWatch, "xpath")
        print("Going to women's watches")
        # self.waitForElement(self._seeMoreBrands, "xpath", 20, 0.5)
        # self.elementClick(self._seeMoreBrands, "xpath")
        # print("Expanding /'See More/' link ")
        self.waitForElement(self._selectBrand, "xpath", 20, 0.5)
        self.elementClick(self._selectBrand, "xpath")
        print("Selected Fossil watches")
        self.waitForElement(self._verifyFilter, "xpath", 20, 0.5)
        filterText = self.getElement(self._verifyFilter, "xpath").text
        print(filterText)
        assert filterText == self._selectedBrand, print("Incorrect Filter")
        print("Correct Filter")

        self.driver.implicitly_wait(5)
        lst = self.driver.find_elements_by_xpath("//div[@id='resultsCol']//ul/li/div/div[2]/div[2]//span[@class='sx-price-whole']")
        print(len(lst))
        priceList = []
        for item in lst:
            priceList.append(item.text)
        priceList.sort()
        print(priceList)
        return True