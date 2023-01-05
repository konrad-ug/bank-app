from behave import *
from selenium.webdriver.common.keys import Keys
import requests
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()
URL = "http://localhost:5000"

@given('Account registry is active')
def make_sure_that_registry_is_working(context):
    resp = requests.get(URL + f"/konta/ile_kont") #jezeli zwróci kod 200 zakładamy ze serwer działa
    assert_equal(resp.status_code, 200)

@when('I create an account using name: {name}, last name: {last_name}, pesel: {pesel}')
def utworz_konto(context, name, last_name, pesel):
    json_body = { "imie": f"{name}",
    "nazwisko": f"{last_name}",
    "pesel": f"{pesel}"
    }
    create_resp = requests.post(URL + "/konta/stworz_konto", json = json_body)
    assert_equal(create_resp.status_code, 201)


@then('Number of accounts in registry equals: "{count}"')
def sprawdz_liczbe_kont_w_rejestrze(context, count):
    ile_kont = requests.get(URL + f"/konta/ile_kont")
    assert_equal(ile_kont.json()["ilosc_kont_w_rejestrze"], int(count))

@step('Account with pesel "{pesel}" exists in registry')
def sprawdz_czy_konto_z_pesel_istnieje(context, pesel):
    #TODO assert czy konto z peselem istnieje
    pass

@step('Account with pesel "{pesel}" does not exists in registry')
def sprawdz_czy_konto_z_pesel_nie_istnieje(context, pesel):
    #TODO assert czy konto z peselem nie istnieje
    pass

@when('I delete account with pesel: "{pesel}"')
def usun_konto(context, pesel):
    #TODO
    pass

@when('I clear the account reagistry')
def usun_wszystkie_konta(context):
    #TODO dopisac endpoint w API i tuttaj go uzyć
    pass