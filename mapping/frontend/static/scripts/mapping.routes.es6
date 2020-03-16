'use strict';

angular.module('mapping.routes')
.config(['$stateProvider', '$urlRouterProvider',
  function ($stateProvider, $urlRouterProvider) {
    $stateProvider
    .state('home', {
      url: '/',
      templateUrl: '/static/templates/layouts/index.layout.html'
    })

    // Pass-through to Django
    .state('signup', { url: '/accounts/signup/' });

    /* Kick them back to the home page if URL is invalid */
    $urlRouterProvider.otherwise('/');
  }
]);
