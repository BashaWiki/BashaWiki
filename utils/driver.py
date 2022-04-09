from selenium import webdriver


class Test_driver:
    chrome_driver_path = "./venv/Scripts/chromedriver.exe"
    edge_driver_path = "./venv/Scripts/msedgedriver.exe"

    def __int__(self):
        pass

    def __init__driver(self, browser):
        if browser == "chrome":
            driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        else:
            driver = webdriver.Edge(executable_path=self.edge_driver_path)
        return driver

    def get_driver(self, browser):
        return self.__init__driver(browser)
