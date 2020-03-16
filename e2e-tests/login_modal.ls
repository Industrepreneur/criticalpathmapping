'use strict'

class LoginModal

  ->
    @email = element by.model 'vm.email'
    @password = element by.model 'vm.password'
    @loginButton = element by.buttonText 'Login'

  get: ->
    browser.get '/'
    @loginButton.click()
    return @

  setEmail: (text) -> @email.sendKeys text; this

  clearEmail: (text) -> @email.clear!; this

  setPassword: (text) -> @password.sendKeys text; this

  clearPassword: (text) -> @password.clear!; this

  submit: -> @loginButton.click!

module.exports = LoginModal
/*export class LoginModal*/
