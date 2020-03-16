'use strict';

/**
 * Sheet list item directive
 * @memberof mapping.sheets.directives.sheet
 */
angular.module('mapping.sheets.directives')
.directive('sheet', sheetDirective);

function sheetDirective() {
  return {
    controller: ['$rootScope', '$scope', '$mdDialog', 'Toast', 'SheetsService', function ($rootScope, $scope, $mdDialog, Toast, Sheets) {
      let vm = this;

      vm.showDeleteSheetDialog = function (ev) {
        ev.stopPropagation();
        alert = $mdDialog.confirm({
          title:       'Are you sure?',
          content:     'This operation cannot be undone.',
          ariaLabel:   'Confirm Deletion',
          ok:          'OK',
          cancel:      'Cancel',
          targetEvent: ev
        });

        $mdDialog.show(alert)
        .then(() => {
          let id          = $scope.sheet.id;
          let description = $scope.sheet.description;
          Sheets.remove(id);
          Toast.show(`Removed sheet #${id} - ${description}`);
          $mdDialog.hide();
        })
        .finally(() => { alert = void 8 });
      };
    }],
    controllerAs: 'vm',
    restrict: 'E',
    scope: {
      sheet: '='
    },
    templateUrl: '/static/templates/sheets/sheet.html'
  };
}
