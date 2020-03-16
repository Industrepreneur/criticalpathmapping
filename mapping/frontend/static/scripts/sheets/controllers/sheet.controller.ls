'use strict'

angular.module 'mapping.sheets.controllers'
    .controller 'SheetController', sheet-controller

sheet-controller.$inject = <[ $rootScope $scope $timeout $log Toast SheetsService part sheet operationMethods operationTypes workPeriods ]>
!function sheet-controller ($rootScope, $scope, $timeout, $log, Toast, Sheets, part, sheet, operationMethods, operationTypes, workPeriods)
    vm = this

    /*Move these to a bootstrap or global process*/
    $rootScope.operationMethods = operationMethods
    $rootScope.operationTypes = operationTypes
    $rootScope.workPeriods = workPeriods

    tabs =
      * title     : 'Detail View'
        chart-type: 'detailView'
      * title     : 'Summary View'
        chart-type: 'summaryView'
      * title     : 'Shop View'
        chart-type: 'shopView'

    selected          = null
    previous          = null

    vm.part           = part
    vm.sheet          = sheet
    vm.tabs           = tabs
    vm.selected-index = 0


    /*Refresh sheet from server after save (not ideal)*/
    $scope.$on \saveCompleted, (event) ->
        Sheets.one sheet.id .then (sheet) !->
            $rootScope.$broadcast \sheet.updated, sheet
            vm.sheet = sheet


    /**
     * Broadcast tab change
     *
     * @memberof mapping.sheets.controllers.SheetController
     * @todo refactor into mapping.sheets.controllers.MapTabsController
     */
    $scope.$watch 'vm.selectedIndex', (current, old) ->
        previous := selected
        selected := tabs[current]

        if selected then $rootScope.$broadcast \tab.selected, selected.chart-type
