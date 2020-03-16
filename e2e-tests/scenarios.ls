'use strict'

describe 'Mapping Authentication', !->

  browser.get '/'

  It 'should have a login link', !->
    expect(element by.buttonText 'Login' .isPresent()).toBe true

  It 'should not display protected links', !->
    expect(element by.buttonText 'Logout' .isPresent()).toBe false
    expect(element by.buttonText 'Parts' .isPresent()).toBe false

  It 'should display login form when clicking login button', !->
    loginButton = element by.buttonText 'Login'
    loginButton.click()
    browser.waitForAngular()
    expect(element by.model 'vm.email' .isPresent()).toBe true
    expect(element by.model 'vm.password' .isPresent()).toBe true
