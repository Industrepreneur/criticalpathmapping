'use strict'

angular.module 'mapping.sheets.controllers'
    .controller 'NewSheetController', NewSheetController

NewSheetController.$inject = <[ $rootScope $scope $stateParams $mdDialog $location $log Toast PartsService SheetsService ]>
!function NewSheetController ($rootScope, $scope, $stateParams, $mdDialog, $location, $log, Toast, Parts, Sheets)
    vm = this

    /**
     * Reset form and close modal dialog
     *
     * @memberof mapping.sheets.controllers.NewSheetController
     */
    cancel = -> $mdDialog.hide!
    vm.cancel = cancel


    /**
     * Create a new Sheet
     *
     * @memberof mapping.sheets.controllers.NewSheetController
     */
    submit = ->
        Parts.one($stateParams.part-id).then (part) ->
            release_date = moment vm.release_date, 'YYYYMMDDHHmm'
            sheet =
                description: vm.description
                release_date: release_date
                raw_materials_estimate: vm.raw_materials_estimate
                logistics_estimate: vm.logistics_estimate
                office_estimate: vm.office_estimate
                finished_goods_estimate: vm.finished_goods_estimate
                part: part

            Sheets.create sheet .then createSheetSuccessFn, createSheetErrorFn
    vm.submit = submit


    function createSheetSuccessFn (data, status, headers, config)
        sheet = data
        $rootScope.$broadcast 'sheet.created', sheet
        $location.url "/parts/#{sheet.part.id}/sheets/#{sheet.id}"
        Toast.show "Added new sheet ##{sheet.id}"
        $mdDialog.hide!


    function createSheetErrorFn (data, status, headers, config)
        $rootScope.$broadcast 'sheet.created.error'
        Toast.error data.data.name.0
