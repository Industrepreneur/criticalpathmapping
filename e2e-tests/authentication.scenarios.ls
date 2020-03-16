'use strict'

require! './home_page.ls': HomePage

describe '', ->
  loginModal = null

  beforeEach ->
    homePage = new HomePage()
    homePage.get()

    loginModal := homePage.clickLogin()

  describe 'login', !->

    It 'should login and redirect to the dashboard with valid credentials', !->
      loginModal
        .setEmail 'manager@widgetco.com'
        .setPassword 'manager'
        .submit()
      browser.waitForAngular()

      expect(browser.getLocationAbsUrl()).toMatch '/'
