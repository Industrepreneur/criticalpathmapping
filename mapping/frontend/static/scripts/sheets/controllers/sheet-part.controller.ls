'use strict'

angular.module 'mapping.sheets.controllers'
    .controller 'SheetPartController', sheet-part-controller

sheet-part-controller.$inject = <[ $scope sheet ]>
!function sheet-part-controller ($scope, sheet)
    vm = this
    vm.sheet = sheet
