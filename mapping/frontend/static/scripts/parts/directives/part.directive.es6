'use strict';

/**
 * The directive to be returned
 * @memberof mapping.parts.directives.part
 */
angular.module('mapping.parts.directives')
.directive('part', partDirective);

function partDirective() {
  return {
    controller: [
      '$scope', '$mdDialog', 'Toast', 'PartsService',
      function ($scope, $mdDialog, Toast, Parts) {
        let vm = this;

        vm.showDeletePartDialog = function (ev) {
          ev.stopPropagation();

          let alert = $mdDialog.confirm({
            title: 'Are you sure?',
            content: 'This operation cannot be undone.',
            ariaLabel: 'Confirm Deletion',
            ok: 'OK',
            cancel: 'Cancel',
            /*controller: 'DeletePartController as vm',*/
            targetEvent: ev
          });

          $mdDialog.show(alert)
          .then(function () {
            let id = $scope.part.id;
            let name = $scope.part.name;
            Parts.remove(id);
            Toast.show(`Removed part #${id} - ${name}`);
            $mdDialog.hide();
          })
          .finally(function () { alert = void 8 });
        };
      }
    ],
    controllerAs: 'vm',
    restrict: 'E',
    scope: { part: '=' },
    templateUrl: '/static/templates/parts/part.html'
  };
}
