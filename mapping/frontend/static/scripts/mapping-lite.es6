'use strict';

// Define main Mapping-Lite application and inject dependencies
angular.module('mapping', [
  'ui.bootstrap',
  'ngMaterial',
  'ngMessages',
  'restangular',
  'mapping.config'
]);

// Load Angular configuration
angular.module('mapping.config', []);

// Ensure Django and Angular CSRF tokens match each others expectations
angular.module('mapping')
.run(['$http', function ($http) {
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  $http.defaults.xsrfCookieName = 'csrftoken';
}]);
