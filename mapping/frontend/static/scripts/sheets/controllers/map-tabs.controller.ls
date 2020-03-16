'use strict'

angular.module 'mapping.sheets.controllers'
    .controller 'MapTabsController', MapTabsController

MapTabsController.$inject = <[ $rootScope $scope $log ]>
!function MapTabsController ($rootScope, $scope, $log)
    vm = this

    tabs =
      * title     : 'Detail View'
        chart-type: 'detailView'
      * title     : 'Summary View'
        chart-type: 'summaryView'
      * title     : 'Shop View'
        chart-type: 'shopView'

    selected = null
    previous = null
    sheet    = $scope.vm.sheet

    vm.sheet          = sheet
    vm.tabs           = tabs
    vm.selected-index = 0

    # $log.debug tabs.sheet

    /**
     * Broadcast tab change
     *
     * @memberof mapping.sheets.controllers.MapTabsController
     */
    $scope.$watch 'vm.selectedIndex', (current, old) ->
        previous := selected
        selected := tabs[current]

        if selected then $rootScope.$broadcast \tab.selected, selected.chart-type
