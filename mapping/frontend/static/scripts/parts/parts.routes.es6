'use strict';

angular.module('mapping.parts.routes')
.config(['$stateProvider',
  function ($stateProvider) {
    $stateProvider
    // Parts Abstract
    .state('parts', {
      abstract: true,
      url: '/parts',
      controller: 'PartsController as vm',
      resolve: {
        Parts: 'PartsService',
        parts: (Parts) => Parts.all()
      },
      template: '<ui-view/>'
    })

    // Parts : /parts
    .state('parts.index', {
      url: '',
      templateUrl: '/static/templates/layouts/parts.layout.html'
    })

    // Part : /parts/:partId
    .state('parts.detail', {
      url: '/{partId:int}',
      controller: 'PartController as vm',
      resolve: {
        Parts: 'PartsService',
        Sheets: 'SheetsService',
        part: ($stateParams, Parts) => { return Parts.one($stateParams.partId) },
        sheets: ($stateParams, Sheets) => { return Sheets.forPart($stateParams.partId) }
      },
      templateUrl: '/static/templates/layouts/part.layout.html'
    });
  }
]);
