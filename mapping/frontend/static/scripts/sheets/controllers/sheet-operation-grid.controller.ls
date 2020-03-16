'use strict'

angular.module 'mapping.sheets.controllers'
    .controller 'SheetOperationGridController', SheetOperationGridController

SheetOperationGridController.$inject = <[ $rootScope $scope $q $mdDialog $log Toast sheet OperationsService operations ]>
!function SheetOperationGridController ($rootScope, $scope, $q, $mdDialog, $log, Toast, sheet, Operations, operations)
    vm = this

    /**
     * Configuration for ez-datetime-picker
     */
    $scope.ez-datetime-config =
        meridiem-enabled : false
        minute-step      : 5
        hour-format      : 'HH'
        view-format      : 'YYYY-MM-DD HH:mm'
        min-date         : moment sheet.release_date # Hack the release_date in (@todo: Move to sheets.service)


    vm.grid-options =
        enable-sorting       : false
        enable-column-menus  : false
        flat-entity-access   : true
        infinite-scroll-down : false
        # show-grid-footer   : true
        # header-template    : 'header_template.html'


    date-cell-template =
        "<div layout=\"row\"" +
        "    layout-align=\"center center\"" +
        "    class=\"ui-grid-cell-contents\"" +
        "    title=\"TOOLTIP\">" +
        "    <div flex>{{MODEL_COL_FIELD | date:'yyyy-MM-dd HH:mm'}}</div>" +
        "    <div ng-if=\"row.entity.operation_type && row.entity.work_period && row.entity.operation_method\">" +
        "        <a ez-datetime-control=\"\"" +
        "          ng-model=\"MODEL_COL_FIELD\"" +
        "          ng-change=\"grid.appScope.saveDate()\"" +
        "          min-date=\"grid.appScope.ezDatetimeConfig.minDate\"" +
        "          config=\"grid.appScope.ezDatetimeConfig\">" +
        "            <span class=\"fa fa-calendar-o\"></span>" +
        "        </a>" +
        "    </div>" +
        "</div>"

    date-cell-button-template =
        "<div class=\"ui-grid-cell-contents\" title=\"TOOLTIP\">" +
        "    <a ez-datetime-control=\"\"" +
        "      ng-model=\"MODEL_COL_FIELD\"" +
        "      ng-change=\"grid.appScope.saveDate()\"" +
        "      on-change=\"grid.appScope.saveDate()\"" +
        "      min-date=\"grid.appScope.ezDatetimeConfig.minDate\"" +
        "      config=\"grid.appScope.ezDatetimeConfig\">" +
        "        <span class=\"fa fa-calendar-o\"></span>" +
        "    </a>" +
        "</div>"

    date-cell-edit-template =
        "<div>" +
        "    <form name=\"inputForm\">" +
        "        <input type=\"text\"" +
        "          ng-class=\"'colt' + col.uid\"" +
        "          ui-grid-editor=\"\"" +
        "          ng-model=\"MODEL_COL_FIELD\"" +
        "          ng-change=\"grid.appScope.formatDate()\"" +
        "          ui-mask=\"9999-99-99 99:99\"" +
        "          placeholder=\"YYYY-MM-DD HH:MM\">" +
        "    </form>" +
        "</div>"

    date-cell-range-template =
        "<div class=\"ui-grid-cell-contents\" title=\"TOOLTIP\">" +
        "    <a ez-datetime-range-control=\"\"" +
        "      class=\"ng-binding ng-isolate-scope ez-datetime-control\"" +
        "      from=\"row.entity.date_started\"" +
        "      to=\"row.entity.date_completed\"" +
        "      on-change=\"grid.appScope.saveDate()\"" +
        "      config=\"grid.appScope.ezDatetimeConfig\">" +
        "        <span class=\"fa fa-calendar-o\"></span>" +
        "    </a>" +
        "</div>"

    delete-operation-template =
        "<div class=\"ui-grid-cell-contents\" title=\"TOOLTIP\">" +
        "    <a ng-if=\"COL_FIELD\"" +
        "      ng-click=\"grid.appScope.showDeleteOperationDialog($event, COL_FIELD)\">" +
        "        <md-icon md-font-icon=\"fa fa-lg fa-fw fa-trash-o\"" +
        "          alt=\"Delete Operation\">" +
        "        </md-icon>" +
        "    </a>" +
        "</div>"


    vm.grid-options.data = operations

    vm.grid-options.column-defs =
        # * name                        : 'operationId'
        #   field                       : 'id'
        #   display-name                : 'ID'
        #   width                       : 30
        #   allow-cell-focus            : false
        * name                        : 'operationType'
          field                       : 'operation_type'
          display-name                : 'Type'
          cell-filter                 : 'operationType'
          editable-cell-template      : 'ui-grid/dropdownEditor'
          edit-dropdown-options-array : $scope.operation-types
          edit-dropdown-value-label   : 'name'
          width                       : 120
        * name                        : 'workPeriod'
          field                       : 'work_period'
          display-name                : 'Period'
          cell-filter                 : 'workPeriod'
          editable-cell-template      : 'ui-grid/dropdownEditor'
          edit-dropdown-options-array : $scope.work-periods
          edit-dropdown-value-label   : 'name'
          width                       : 120
        * name                        : 'operationMethod'
          field                       : 'operation_method'
          display-name                : 'Method'
          cell-filter                 : 'operationMethod'
          editable-cell-template      : 'ui-grid/dropdownEditor'
          edit-dropdown-options-array : $scope.operation-methods
          edit-dropdown-value-label   : 'name'
          width                       : 120
        * name                        : 'dateStarted'
          field                       : 'date_started'
          edit-model-field            : 'string_started'
          display-name                : 'Start Date'
          cell-template               : date-cell-template
          editable-cell-template      : date-cell-edit-template
          enable-column-resizing      : false
          width                       : 125
        * name                        : 'dateCompleted'
          field                       : 'date_completed'
          edit-model-field            : 'string_completed'
          display-name                : 'End Date'
          cell-template               : date-cell-template
          editable-cell-template      : date-cell-edit-template
          enable-column-resizing      : false
          width                       : 125
        #* name                        : 'btn2'
        # display-name                 : '2'
        # enable-cell-edit             : false
        # enable-cell-edit-on-focus    : false
        # cell-template                : date-cell-button-template
        #* name                        : 'btn'
        # display-name                 : ''
        # enable-cell-edit             : false
        # enable-cell-edit-on-focus    : false
        # cell-template                : date-cell-range-template
        # /*maxWidth                   : 25*/
        # /*minWidth                   : 25*/
        # width                        : 25
        * name                        : 'quantityIn'
          field                       : 'quantity_in'
          display-name                : 'In'
          editable-cell-template      : "<div><form name=\"inputForm\"><input type=\"number\" min=\"1\" ng-class=\"'colt' + col.uid\" ui-grid-editor ng-model=\"MODEL_COL_FIELD\"></form></div>"
          enable-column-resizing      : false
          width                       : 45
        * name                        : 'quantityOut'
          field                       : 'quantity_out'
          display-name                : 'Out'
          editable-cell-template      : "<div><form name=\"inputForm\"><input type=\"number\" min=\"1\" max=\"{{row.entity.quantity_in}}\" ng-class=\"'colt' + col.uid\" ui-grid-editor ng-model=\"MODEL_COL_FIELD\"></form></div>"
          enable-column-resizing      : false
          width                       : 45
        * name                        : 'description'
          field                       : 'description'
          display-name                : 'Description'
        * name                        : 'delete'
          display-name                : ''
          field                       : 'id'
          cell-template               : delete-operation-template
          allow-cell-focus            : false
          enable-cell-edit            : false
          enable-column-resizing      : false
          width                       : 25


    /**
     * Update date field from unformatted input value
     */
    $scope.format-date = ->
        cell         = vm.grid-api.cell-nav.get-focused-cell!
        row-entity   = cell.row.entity
        col-def      = cell.col.col-def
        date-field   = col-def.field
        date-value   = row-entity[date-field]
        string-field = col-def.edit-model-field
        string-value = row-entity[string-field]
        m            = moment string-value, 'YYYYMMDDHHmm'
        if m.is-valid! then row-entity[date-field] = m.format!


    /**
     * Trigger ui-grid saveRow on datepicker entry
     * Dates need to be wrangled into timezone-specific values before submitting
     * in order to prevent values from "jumping" around.
     */
    $scope.save-date = ->
        cell            = vm.grid-api.cell-nav.get-focused-cell!
        row-entity      = cell.row.entity
        col-def         = cell.col.col-def
        started-value   = row-entity.date_started
        completed-value = row-entity.date_completed


        return unless started-value? and completed-value?
        # @todo UI-Grid need setRowsError method
        if completed-value <= started-value
            cell.row.isError = true
            return

        started-moment              = moment started-value
        row-entity.date_started     = started-moment.format!
        row-entity.string_started   = started-moment.format 'YYYYMMDDHHmm'
        completed-moment            = moment completed-value
        row-entity.date_completed   = completed-moment.format!
        row-entity.string_completed = completed-moment.format 'YYYYMMDDHHmm'
        vm.grid-api.row-edit.set-rows-dirty [row-entity]


    $scope.show-delete-operation-dialog = (ev, id) !->
        ev.stop-propagation!
        cell       = vm.grid-api.cell-nav.get-focused-cell!
        row-entity = cell.row.entity

        alert = $mdDialog.confirm do
            title        : 'Are you sure?'
            content      : 'This operation cannot be undone.'
            aria-label   : 'Confirm Deletion'
            ok           : 'OK'
            cancel       : 'Cancel'
            event-target : ev

        $mdDialog
            .show alert
            .then (data, status, headers, config) !->
                $mdDialog.hide!
                key = _.find-index operations, id: id
                operations[key].remove!then ->
                    operations.splice key, 1
                    $rootScope.$broadcast \saveCompleted
                    Toast.show "Removed operation ##{id}"

            .finally -> alert = void

    vm.grid-options.on-register-api = (grid-api) ->
        vm.grid-api = grid-api

        grid-api.edit.on.begin-cell-edit $scope, (rowEntity, colDef, event) ->
            /*If cell-edit is triggered by F1 through F12 then move cursor to end of text*/
            if event && event.type is 'keydown' and event.key-code in [112 to 123]
                /*Delay selection to make sure we get the proper DOM element*/
                set-timeout ->
                    el = document.activeElement
                    if el.tagName.toLowerCase! is 'input'
                        # Stupid W3C: https://www.w3.org/Bugs/Public/show_bug.cgi?id=24796
                        el.type = 'text' if el.type in ['number', 'email']
                        len     = el.value.length
                        el.setSelectionRange len, len

        grid-api.row-edit.on.save-row $scope, $scope.save-row


    for row in vm.grid-options.data
        started-moment   = moment row.date_started
        completed-moment = moment row.date_completed

        /*Update date values with local timezone*/
        row.date_started   = started-moment.format!
        row.date_completed = completed-moment.format!

        /*Created unformatted string datefields for masked entry*/
        row.string_started   = started-moment.format 'YYYY-MM-DD HH:mm'
        row.string_completed = completed-moment.format 'YYYY-MM-DD HH:mm'

    /*Add initial empty row*/
    add-empty-row!


    /**
     * Create or Update a row
     * @param {Object} row - Row Entity to be saved
     */
    $scope.save-row = (row) ->
        id               = row.id or null
        string_started   = row.string_started or null
        string_completed = row.string_completed or null

        row.quantity_in  = 1 unless row.quantity_in?
        row.quantity_out = 1 unless row.quantity_out?

        if row.date_competed <= row.date_started
            cell.row.isError = true

        if string_started?
            row.date_started = moment string_started, 'YYYYMMDDHHmm' .format!

        if string_completed?
            row.date_completed = moment string_completed, 'YYYYMMDDHHmm' .format!

        if id?
            /*Save an existing row*/
            operation = row.save!then ->
                # @todo remove old callbacks
                $rootScope.$broadcast \saveCompleted
                $rootScope.$broadcast \operation.saved
        else
            /*Save a new row*/
            unless row.operation_type? and row.work_period? and row.operation_method? and row.date_started? and row.date_completed?
                /*create fake promise on incomplete data*/
                promise = $q.defer!
                vm.grid-api.row-edit.set-save-promise row, promise.promise
                return promise.resolve!

            row.sheet = sheet
            operation = Operations.create row .then (new-row) ->
                # @todo remove old callbacks
                $rootScope.$broadcast \saveCompleted
                $rootScope.$broadcast \operation.saved
                /*Replace grid operation with newly saved row*/
                vm.grid-options.data[*-1] = new-row
                add-empty-row!

        return unless operation?
        vm.grid-api.row-edit.set-save-promise row, operation


    /**
     * Insert empty row at end of grid data
     */
    function add-empty-row
        if operations.length is 0 or (operations[*-1]? and operations[*-1].id?)
            vm.grid-options.data.push {}
