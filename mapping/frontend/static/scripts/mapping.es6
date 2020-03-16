'use strict';

// Define main Mapping application and inject dependencies
angular.module('mapping', [
  'ui.bootstrap',
  'ui.mask',
  'ez.dropdown',
  'ez.datetime',
  'ngMaterial',
  'restangular',
  'ui.grid',
  'ui.grid.edit',
  'ui.grid.rowEdit',
  'ui.grid.cellNav',
  'ui.grid.resizeColumns',
  'mapping.auth',
  'mapping.config',
  'mapping.controllers',
  'mapping.routes',
  'mapping.utils',
  'mapping.accounts',
  'mapping.charts',
  'mapping.operations',
  'mapping.parts',
  'mapping.sheets'
]);

// Load Angular configuration
angular.module('mapping.config', []);

// Define Controllers application
angular.module('mapping.controllers', []);

// Define Routes application
angular.module('mapping.routes', ['ui.router']);

// Ensure Django and Angular CSRF tokens match each others expectations
angular.module('mapping')
.run(['$http', function ($http) {
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  $http.defaults.xsrfCookieName = 'csrftoken';
}])

// // Log state-change errors to help with ui-router resolve issues
// .run(['$rootScope', '$log', function ($rootScope, $log) {
//   $rootScope.$on('$stateChangeError', (event, toState, toParams, fromState, fromParams, error) => {
//     // $log.error(error);
//   });
// }])

// Inject UI-Router state into $rootScope
.run(['$rootScope', '$state', '$stateParams', function ($rootScope, $state, $stateParams) {
  $rootScope.$state = $state;
  $rootScope.$stateParams = $stateParams;
}])

// Inject lodash into Angular scope as a constant for DI in controllers and tests
.constant('_', window._)

// Inject lodash into $rootScope for use in views (eg. ng-repeat="x in _.range(3)")
.run(['$rootScope', function ($rootScope) { $rootScope._ = window._; }])

// Inject moment.js into Angular scope...
.constant('moment', window.moment)
.run(['$rootScope', function ($rootScope) { $rootScope.moment = window.moment; }])

// Inject oCanvas into global scope...
.constant('oCanvas', window.oCanvas)
.run(['$rootScope', function ($rootScope) { $rootScope._oCanvas = window.oCanvas; }])

// Add constants for the days of the week
.constant('DAYS', {
  SUNDAY: 0,
  MONDAY: 1,
  TUESDAY: 2,
  WEDNESDAY: 3,
  THURSDAY: 4,
  FRIDAY: 5,
  SATURDAY: 6
});
