from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    btnFlights = (By.CLASS_NAME, "FLIGHTS")


    def btnFlighMethod(self):
        return self.driver.find_element(*HomePage.btnFlights)



