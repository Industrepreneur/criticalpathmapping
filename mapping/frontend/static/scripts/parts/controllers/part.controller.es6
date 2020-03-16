'use strict';

angular.module('mapping.parts.controllers')
.controller('PartController', partController);

partController.$inject = ['$scope', '$mdDialog', 'part', 'sheets'];
function partController ($scope, $mdDialog, part, sheets) {
  let vm = this;

  $scope.$on('sheet.created', (event, sheet) => { vm.sheets.unshift(sheet) });
  $scope.$on('sheet.deleted', (event, id) => { _.remove(vm.sheets, 'id', id) });

  vm.showNewSheetDialog = function (ev) {
    $mdDialog.show({
      controller: 'NewSheetController as vm',
      templateUrl: '/static/templates/sheets/new-sheet.html',
      targetEvent: ev
    });
  };

  vm.part = part;
  vm.sheets = sheets;
}
