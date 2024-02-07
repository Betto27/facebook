Feature: Acessar o Facebook

  @pesquisar
  Scenario: Pesquisar no google e acessar o facebook
    Given que faço uma pesquisa no google por https://www.google.com
    When clico no link do facebook
    Then acesso o site do facebook