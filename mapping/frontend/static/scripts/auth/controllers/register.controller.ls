'use strict'

angular.module 'mapping.auth.controllers'
    .controller 'RegisterController', register-controller

register-controller.$inject = <[ $scope $location $log AuthService ]>
!function register-controller ($scope, $location, $log, Auth)
    init = !-> $location.url '/' if Auth.is-authenticated!


    register-success-fn = (data, status, headers, config) !->
        Auth.login vm.email, vm.password


    register-error-fn = (data, status, headers, config) !->
        # $log.error 'Critical failure!'


    register = (email, password) !->
        $http.post '/api/v1/users/', { email: email, password: password }
            .then register-success-fn, register-error-fn

    vm = this
    vm.register = register
    init!
