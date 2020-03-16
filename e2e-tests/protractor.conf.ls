require 'LiveScript'

exports.config =
  allScriptsTimeout: 11000,

  specs: [
    '*.scenarios.ls'
  ]

  capabilities:
    'browserName': 'chrome'

  baseUrl: 'http://192.168.99.100'

  framework: 'jasmine2'

  jasmineNodeOpts:
    defaultTimeoutInterval: 30000

  /*it is a reserved keyword in LiveScript*/
  onPrepare: ->
    global.It = global.it
    global.xIt = global.xit
