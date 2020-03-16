'use strict'

require! './login_modal.ls': LoginModal

export class HomePage
  ->
    @loginLink = element by.buttonText 'Login'

  get: ->
    browser.get '/'
    return @

  clickLogin: ->
    @loginLink.click()
    browser.waitForAngular()
    new LoginModal()
