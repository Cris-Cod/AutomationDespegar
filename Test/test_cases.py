import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.homePage import HomePage
from POM.vuelos import Vuelos
from utilities.BaseClass import BaseClass


class TestCases(BaseClass):
    titleVuelos = "Vuelos"
    ciudadOrigen = "Iba"
    ciudad = "Ibagué, Tolima, Colombia"
    mes = "noviembre"
    anio = "2024"
    dia = 10
    mesArrived = "diciembre"
    anioArrived = "2024"
    quantityPassanger = 3
    passangerAdult = 1
    quantityPassangerChilden = 2
    passangerChildren = 0
    childrenAge1 = "5 años"
    childrenAge2 = "8 años"
    classOption = "Premium economy"

    def test_buy_flilights_city_with_3_letters(self):
        homePage = HomePage(self.driver)
        vuelosPage = Vuelos(self.driver)
        #homePage.btnFlighMethod().click()
        #self.verifyLinkPresence("Vuelos")
        #text = vuelosPage.txtVuelosMethod().text
        #assert TestCases.titleVuelos == text
        vuelosPage.originMethod().click()
        vuelosPage.originMethod().clear()
        city = vuelosPage.originMethod()
        city.send_keys("Iba")
        #city.send_keys(Keys.ENTER)
        #self.verifyLinkPresence("Ibagué, Tolima, Colombia")
        ciudad_elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//ul[@class='ac-group-items']/li[1]//a[contains(text(), '{TestCases.ciudad}')]"))
        )
        ciudad_elemento.click()
        #city.send_keys(Keys.ENTER)

        """ciudad_elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//ul[@data-stid='flight-origin-results']//a[contains(text(), '{ciudad}')]"))
        )
        ciudad_elemento.click()"""

    def test_buy_flilights_city_full_letters(self):

        homePage = HomePage(self.driver)
        homePage.btnFlighMethod().click()
        vuelosPage = Vuelos(self.driver)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(vuelosPage.originMethod()))
        vuelosPage.originMethod().click()
        vuelosPage.originMethod().clear()
        originField = vuelosPage.originMethod()
        originField.send_keys("Ibague")
        self.times(1)
        originField.send_keys(Keys.ENTER)
        vuelosPage.destinyMethod().click()
        vuelosPage.destinyMethod().clear()
        cityDestiny = vuelosPage.destinyMethod()
        cityDestiny.send_keys("Milan")
        self.times(2)
        cityDestiny.send_keys(Keys.ENTER)


        vuelosPage.btnCalendarMethod().click()
        while True:
            month = vuelosPage.calendarMonthMethod().text
            year = vuelosPage.calendarYearMethod().text
            if month.lower() == TestCases.mes and year == TestCases.anio:
                break
            else:
                vuelosPage.calendarArrowRightMethod().click()

        vuelosPage.calendarDayGoMethod().click()

        while True:
            month = vuelosPage.calendarMonthMethod().text
            year = vuelosPage.calendarYearMethod().text
            if month.lower() == TestCases.mesArrived and year == TestCases.anioArrived:
                break
            else:
                vuelosPage.calendarArrowRightMethod().click()

        vuelosPage.calendarDayGoMethod().click()

        vuelosPage.passangerMethod().click()

        while True:
            if TestCases.passangerAdult == TestCases.quantityPassanger:
                break
            else:
                vuelosPage.adultsButtonPlusMethod().click()

            TestCases.passangerAdult += 1


        while True:
            if TestCases.passangerChildren == TestCases.quantityPassangerChilden:
                break
            else:
                vuelosPage.childerButtonPlusMethod().click()

            TestCases.passangerChildren += 1


        self.selectByText(vuelosPage.dropdownAgeChildren1Method(), TestCases.childrenAge1)
        self.selectByText(vuelosPage.dropdownAgeChildren2Method(), TestCases.childrenAge2)
        self.selectByText(vuelosPage.dropdownClassMethod(), TestCases.classOption)

        vuelosPage.btnApplyMethod().click()
        vuelosPage.btnSearchMethod().click()

        self.element_is_visible(vuelosPage.txtVuelosMethod())



