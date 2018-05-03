# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
from time import sleep
import os



name = "Krystyna"
surname = "Nowak"
PESEL = "87040885925"
mother_name = "Anna"
father_name = "Jan"
mother_surname = "Kowalska"
place_of_birth = "Warszawa"
email = "k.nowak000000000000@gmail.com"
telephone = "566 789 555"
street = u"Marszałkowska"
building_number = "5"
apartment_number = "22"
postal_code = "22-090"
city = "Warszawa"
identity_card_number = "XVY858270"
identity_card_expiration_date = "31-12-2018"
photo_path = os.getcwd() + "/photo.jpg"
upload_file_error_message = u"Plik jest zbyt duży."


class EurobankRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_invalid_photo(self):
        driver = self.driver
        driver.get("https://eurobank.pl")
        sleep(5)
        kont_os_btn = driver.find_element_by_css_selector(".otworz-konto > a:nth-child(1)")
        kont_os_btn.click()
        sleep(5)
        przelew_btn = driver.find_element_by_id ("contractconclusionmethod_przelew")
        przelew_btn.click()

        przejdz_dalej_btn = driver.find_element_by_css_selector(".large")
        przejdz_dalej_btn.click()

        wyb_konto_btn = driver.find_element_by_css_selector("#accountType > option:nth-child(3)")
        wyb_konto_btn.click()

        odb_wyc_btn = driver.find_element_by_css_selector("#statementDeliveryMethod > option:nth-child(2)")
        odb_wyc_btn.click()
        bank_int_btn = driver.find_element_by_id("additionalInternetTransactionSecurity")
        bank_int_btn.click()

        wyb_karty_btn = driver.find_element_by_xpath('//input[@value="VISA_ELECTRON"]')
        wyb_karty_btn.click()

        #apl_mob_btn = driver.find_element_by_css_selector('#wantToUseMobileApp > option:nth-child(2)')
        apl_mob_btn = driver.find_element_by_xpath('//select[@id="wantToUseMobileApp"]/option[@value="yes"]')
        apl_mob_btn.click()
        dalej_btn = driver.find_element_by_css_selector('button.btn')
        dalej_btn.click()
        name_field = driver.find_element_by_id("firstName")
        name_field.send_keys(name)
        surname_field = driver.find_element_by_id("lastName")
        surname_field.send_keys(surname)
        PESEL_field = driver.find_element_by_id("pesel")
        PESEL_field.send_keys(PESEL)
        mother_name_field = driver.find_element_by_id("motherFirstName")
        mother_name_field.send_keys(mother_name)
        father_name_field = driver.find_element_by_id("fatherFirstName")
        father_name_field.send_keys(father_name)
        mother_surname_field = driver.find_element_by_id("motherMaidenName")
        mother_surname_field.send_keys(mother_surname)

        place_of_birth_field = driver.find_element_by_id("birthPlace")
        place_of_birth_field.send_keys(place_of_birth)
        birth_country_btn = driver.find_element_by_xpath('//select[@id="birthCountry"]/option[@value="POLSKA"]')
        birth_country_btn.click()
        nationality_btn = driver.find_element_by_id("nationality")
        nationality_btn.click()
        country_of_residence_btn = driver.find_element_by_id("countryOfResidence")
        country_of_residence_btn.click()
        source_of_income_btn = driver.find_element_by_xpath('//select[@id="sourceOfIncome"]/option[@value="PRACOWNIK"]')
        source_of_income_btn.click()
        pol_tax_residence_btn = driver.find_element_by_css_selector("#isPoland > option:nth-child(2)")
        pol_tax_residence_btn.click()
        oth_tax_res_btn = driver.find_element_by_css_selector("#isOther > option:nth-child(3)")
        oth_tax_res_btn.click()
        citizen_USA_btn = driver.find_element_by_xpath('//select[@id="isUsa"]/option[@value="no"]')
        citizen_USA_btn.click()
        telefon_field = driver.find_element_by_id("cellPhoneNumber")
        telefon_field.send_keys(telephone)
        email_field = driver.find_element_by_id("email")
        email_field.send_keys(email)
        street_field = driver.find_element_by_id("registerredAddress_street")
        street_field.send_keys(street)
        build_numb_field = driver.find_element_by_id("registerredAddress_buildingNumber")
        build_numb_field.send_keys(building_number)
        ap_numb_field = driver.find_element_by_id("registerredAddress_apartmentNumber")
        ap_numb_field.send_keys(apartment_number)
        post_code_field = driver.find_element_by_id("registerredAddress_postalCode")
        post_code_field.send_keys(postal_code)
        city_field = driver.find_element_by_id("registerredAddress_town")
        city_field.send_keys(city)
        province_btn = driver.find_element_by_xpath('//select[@id="registerredAddress_province"]/option[@value="MAZOWIECKIE"]')
        province_btn.click()
        cores_adr_btn = driver.find_element_by_id('correspondenceAddressTheSameAsRegisterredAddress')
        if not cores_adr_btn.is_selected():
            cores_adr_btn.click()
        privacy_policy_btn = driver.find_element_by_id('agreementToReceiveCommercialInformation')
        if not privacy_policy_btn.is_selected():
            privacy_policy_btn.click()
        dalej_btn = driver.find_element_by_css_selector('button.btn')
        dalej_btn.click()
        id_card_btn = driver.find_element_by_xpath('//select[@id="identityDocumentType"]/option[@value="DOWOD_OSOBISTY"]')
        id_card_btn.click()
        id_card_number = driver.find_element_by_id("identityCardNumber")
        id_card_number.send_keys(identity_card_number)
        identity_card_exp_date = driver.find_element_by_id("identityCardExpirationDate")
        identity_card_exp_date.click()
        identity_card_exp_date.send_keys(identity_card_expiration_date)

        upload_file_avers = driver.find_element_by_xpath("//div[@id='container_file_avers']//input[@type='file']")
        upload_file_avers.send_keys(photo_path)
        upload_file_revers = driver.find_element_by_xpath("//div[@id='container_file_revers']//input[@type='file']")
        upload_file_revers.send_keys(photo_path)

        error_avers = driver.find_element_by_id("error_avers")
        error_revers = driver.find_element_by_id("error_revers")

        print(error_avers.text)
        print(error_revers.text)

        self.assertEqual(error_avers.text, upload_file_error_message)
        self.assertEqual(error_revers.text, upload_file_error_message)

        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
            unittest.main(verbosity = 2)
