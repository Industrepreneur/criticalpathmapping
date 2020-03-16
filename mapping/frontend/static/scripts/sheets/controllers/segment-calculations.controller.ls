angular.module 'mapping.sheets.controllers'
    .controller 'SegmentCalculationsController', segment-calculations-controller

segment-calculations-controller.$inject = <[ $rootScope $scope $timeout Toast $log SheetsService sheet ]>
!function segment-calculations-controller ($rootScope, $scope, $timeout, Toast, $log, Sheets, sheet)
    vm = this
    vm.sheet = sheet
    timeout = null

    save-updates = !->
        if $scope.segmentEstimatesForm.$valid
            save-started!
            Sheets.save(sheet) .then (response) !-> save-finished!
        else
            Toast.error 'invalid data'

    save-started = !-> $rootScope.$broadcast \saveInProgress, true

    save-finished = !->
        $rootScope.$broadcast \saveInProgress, false
        $rootScope.$broadcast \saveCompleted

    debounce-save = (new-val, old-val) !->
        if new-val isnt old-val
            if timeout then $timeout.cancel timeout
            timeout := $timeout save-updates, 1000

    $scope.$watch 'vm.sheet.raw_materials_estimate', debounce-save
    $scope.$watch 'vm.sheet.logistics_estimate', debounce-save
    $scope.$watch 'vm.sheet.office_estimate', debounce-save
    $scope.$watch 'vm.sheet.finished_goods_estimate', debounce-save
