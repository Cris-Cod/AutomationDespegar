from selenium.webdriver.common.by import By


class Vuelos:
    def __init__(self, driver):
        self.driver = driver

    txtVuelos = (By.XPATH, "//div[@class='sbox5-box-header--2c4hh']/h1")
    origin = (By.CSS_SELECTOR, "input[placeholder='Ingresa desde dónde viajas']")
    destiny = (By.CSS_SELECTOR, "input[placeholder='Ingresa hacia dónde viajas']")
    btnCalendar = (By.CSS_SELECTOR, "div[class='sbox5-dates-component--3dTHh']")
    calendarGo = (By.CSS_SELECTOR, "input[placeholder='Ida']")
    calendarBack = (By.CSS_SELECTOR, "input[placeholder='Vuelta']")
    calendarArrowLeft = (By.CSS_SELECTOR, "a[class='calendar-arrow-left ']")
    calendarArrowRight = (By.CSS_SELECTOR, "a[class='calendar-arrow-right ']")
    calendarMonth = (By.XPATH, "//div[@class='calendar-container ']/div[1]/div/div[1]")
    calendarYear = (By.XPATH, "//div[@class='calendar-container ']/div[1]/div/div[2]")
    calendarDayGo = (By.XPATH, "//div[@class='calendar-container ']/div[2]/div[3]/div[10]")
    passanger = (By.CSS_SELECTOR, "div[class='sbox5-passengers-distribution-container']")
    adultsButtonPlus = (By.XPATH, "//div[@class='stepper__distribution_container']/div[1]/div[2]/div/button[2]")
    childerButtonPlus = (By.XPATH, "//div[@class='stepper__distribution_container']/div[2]/div[2]/div/button[2]")
    dropdownAgeChildren1 = (By.XPATH, "//div[@class='stepper__distribution_container']/div[3]/div[2]/div/div/select")
    dropdownAgeChildren2 = (By.XPATH, "//div[@class='stepper__distribution_container']/div[4]/div[2]/div/div/select")
    dropdownClass = (By.XPATH, "//div[@class='sbox5-3-select -lg']/div/select")
    btnApply = (By.XPATH, "//div[@class='stepper__room__footer ']/a")
    btnSearch = (By.XPATH, "//div[@class='sbox5-button-container--1X4O8']/button")
    txtEscacla = (By.XPATH, "//div[@class='filter-container']/span/filters/div/div/ul/filter-group[1]/li/span")

    def txtVuelosMethod(self):
        return self.driver.find_element(*Vuelos.txtVuelos)

    def originMethod(self):
        return self.driver.find_element(*Vuelos.origin)

    def destinyMethod(self):
        return self.driver.find_element(*Vuelos.destiny)

    def calendarGoMethod(self):
        return self.driver.find_element(*Vuelos.calendarGo)

    def calendarBackMethod(self):
        return self.driver.find_element(*Vuelos.calendarBack)

    def calendarArrowLeftMethod(self):
        return self.driver.find_element(*Vuelos.calendarArrowLeft)

    def calendarArrowRightMethod(self):
        return self.driver.find_element(*Vuelos.calendarArrowRight)

    def calendarMonthMethod(self):
        return self.driver.find_element(*Vuelos.calendarMonth)

    def calendarYearMethod(self):
        return self.driver.find_element(*Vuelos.calendarYear)

    def calendarDayGoMethod(self):
        return self.driver.find_element(*Vuelos.calendarDayGo)

    def passangerMethod(self):
        return self.driver.find_element(*Vuelos.passanger)

    def adultsButtonPlusMethod(self):
        return self.driver.find_element(*Vuelos.adultsButtonPlus)

    def childerButtonPlusMethod(self):
        return self.driver.find_element(*Vuelos.childerButtonPlus)

    def dropdownAgeChildren1Method(self):
        return self.driver.find_element(*Vuelos.dropdownAgeChildren1)

    def dropdownAgeChildren2Method(self):
        return self.driver.find_element(*Vuelos.dropdownAgeChildren2)

    def dropdownClassMethod(self):
        return self.driver.find_element(*Vuelos.dropdownClass)

    def btnApplyMethod(self):
        return self.driver.find_element(*Vuelos.btnApply)

    def btnSearchMethod(self):
        return self.driver.find_element(*Vuelos.btnSearch)

    def txtEscaclaMethod(self):
        return self.driver.find_element(*Vuelos.txtEscacla)

    def btnCalendarMethod(self):
        return self.driver.find_element(*Vuelos.btnCalendar)