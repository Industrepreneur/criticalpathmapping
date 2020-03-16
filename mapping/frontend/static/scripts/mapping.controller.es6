'use strict';

angular.module('mapping.controllers').controller('AppController', appController);

appController.$inject = ['$scope', '$window', '$mdDialog', '$log', 'AuthService'];

function appController($scope, $window, $mdDialog, $log, Auth) {
  let vm = this;

  /**
   * Retrieve the current datetime
   */
  vm.date = new Date();

  vm.isLoggedIn = Auth.isAuthenticated();

  /**
   * Logout current user
   */
  vm.logout = function () { Auth.logout() };

  /**
   * Redirect to django admin site
   */
  vm.gotoAdmin = function () { $window.location.href = '/admin' };

  /**
   * Redirect to django backend admin site
   */
  vm.gotoBackend = function () { $window.location.href = '/backend' };

  vm.login = function () {
    let email = vm.email.toLowerCase();
    Auth.login(email, vm.password);
  };

  /**
   * Display the signup page
   */
  vm.openSignupPage = function () { $window.location.href = '/accounts/signup/' };

  /**
   * Display the user guide
   */
  vm.openUserGuide = function () {
    $window.open('http://mymanufacturing.org/CPM/guide/', '_blank');
  };

  /**
   * Display login form in a modal dialog
   * @param {Object} ev - Trigger event
   */
  vm.showLoginDialog = function (event) {
    $mdDialog.show({
      controller: 'LoginController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/auth/login.html',
      targetEvent: event
    });
  };

  $scope.$on('saveInProgress', (event, status) => { vm.saveInProgress = status });
}
