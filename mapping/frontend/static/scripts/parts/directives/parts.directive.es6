'use strict';

/**
 * The directive to be returned
 * @memberof mapping.parts.directives.parts
 */
angular.module('mapping.parts.directives')
.directive('parts', partsDirective);

partsDirective.$inject = ['$mdDialog'];

function partsDirective($mdDialog) {
  return {
    controller: function () {
      let vm = this;

      vm.showNewPartDialog = function (event) {
        $mdDialog.show({
          controller: 'NewPartController as vm',
          templateUrl: '/static/templates/parts/new-part.html',
          targetEvent: event
        });
      };
    },
    controllerAs: 'vm',
    restrict: 'E',
    scope: { parts: '=' },
    templateUrl: '/static/templates/parts/parts.html'
  };
}
