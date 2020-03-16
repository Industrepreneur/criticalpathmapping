'use strict';

angular.module('mapping.config')
.config(['$locationProvider', function ($locationProvider) {
  // Enable HTML5 hash-free URLs
  $locationProvider.html5Mode(true);

  // Change hash prefix for search engine porpoises
  $locationProvider.hashPrefix('!');
}])

.config(['RestangularProvider', function (RestangularProvider) {
  // Set the API endpoint root
  RestangularProvider.setBaseUrl('/api/v1');
}])

.config(['$mdIconProvider', function ($mdIconProvider) {
  // Configure URLs for icons specified by [set:]id
  $mdIconProvider.defaultFontSet('fontawesome');
}])

.config(['$mdThemingProvider', function ($mdThemingProvider) {
  let fcBlueMap, fcOrangeMap;

  // Configure theme for Material Design
  fcBlueMap = $mdThemingProvider.extendPalette('blue-grey', {
    '50': 'cfd8dc',
    '500': '22246F',
    'A100': 'eeeeee',
    'contrastDefaultColor': 'light',
    'contrastDarkColors': ['50', '100', '200', '300', '400', 'A100']
  });

  fcOrangeMap = $mdThemingProvider.extendPalette('orange', {
    'A200': 'FFA500',
    'contrastDefaultColor': 'light'
  });

  $mdThemingProvider.definePalette('fc-blue', fcBlueMap);
  $mdThemingProvider.definePalette('fc-orange', fcOrangeMap);

  $mdThemingProvider.theme('default')
  .primaryPalette('fc-blue')
  .accentPalette('fc-orange');
}]);
