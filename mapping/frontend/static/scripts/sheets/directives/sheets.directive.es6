'use strict';

/**
 * @name sheets
 * @desc The directive to be returned
 * @memberOf mapping.sheets.directives.sheets
 */
angular.module('mapping.sheets.directives')
.directive('sheets', sheetsDirective);


function sheetsDirective() {
  return {
    controller: ['$mdDialog', function ($mdDialog) {
      let vm = this;
      vm.showNewSheetDialog = function (ev) {
        $mdDialog.show({
          controller: 'NewSheetController as vm',
          templateUrl: '/static/templates/sheets/new-sheet.html',
          targetEvent: ev
        });
      };
    }],
    controllerAs: 'vm',
    restrict: 'E',
    scope: {
      sheets: '='
    },
    templateUrl: '/static/templates/sheets/sheets.html'
  };
}
