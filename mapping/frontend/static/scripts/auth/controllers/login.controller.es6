'use strict';

angular.module('mapping.auth.controllers')
.controller('LoginController', loginController);

loginController.$inject = ['$scope', '$location', '$log', 'AuthService'];

function loginController ($scope, $location, $log, Auth) {
  let vm = this;

  function init() {
    // if (Auth.isAuthenticated()) {
    //   $log.debug('is authenticated, redirecting');
    //   $location.url('/');
    // }
  }

  vm.login = function () {
    let email = vm.email.toLowerCase();
    Auth.login(email, vm.password);
  };

  init();
}
