from behave import given, when, then
from selenium import webdriver
from nose.tools import assert_equal
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

@given(u'que faço uma pesquisa no google por {url}')
def step_impl(context, url):
    driver.get(url)
    driver.maximize_window()

@when(u'clico no link do {site_pes}')
def step_impl(context, site_pes):
    # Localiza o campo de pesquisa escreve o site que está sendo pesquisado, e finaliza precionando a tecla ENTER do TECLADO
    driver.find_element_by_css_selector(
        'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input').send_keys(
        site_pes + Keys.ENTER)
    # Localiza o link do site e da um click
    driver.find_element_by_css_selector('#tads > div > div > div > div.d5oMvf > a > div.cfxYMc.JfZTW.c4Djg.MUxGbd.v0nnCb').click()

@then(u'acesso o site do facebook')
def step_impl(context):
    assert_equal(driver.title, 'Cadastrar-se no Facebook | Facebook')
