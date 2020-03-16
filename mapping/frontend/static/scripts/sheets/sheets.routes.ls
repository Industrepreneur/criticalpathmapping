'use strict'

angular.module 'mapping.sheets.routes'
.config [
'$stateProvider', '$urlRouterProvider',
($stateProvider, $urlRouterProvider) !->

    $stateProvider

    .state 'sheets',
        abstract: true
        url: '/parts/{partId:int}/sheets/{sheetId:int}'
        resolve:
            Operations: 'OperationsService'
            operations: ($stateParams, Operations) -> Operations.for-sheet $stateParams.sheet-id
            Parts: 'PartsService'
            part: ($stateParams, Parts) -> Parts.one $stateParams.part-id
            Operation-methods: 'OperationMethodsService'
            operation-methods: (Operation-methods) -> Operation-methods.all!
            Operation-types: 'OperationTypesService'
            operation-types: (Operation-types) -> Operation-types.all!
            Sheets: 'SheetsService'
            sheet: ($stateParams, Sheets) -> Sheets.one $stateParams.sheet-id
            Work-periods: 'WorkPeriodsService'
            work-periods: (Work-periods) -> Work-periods.all!
        controller: 'SheetController as vm'
        template-url: '/static/templates/layouts/sheet.layout.html'

    # Sheet : /parts/:partId/sheets/:sheetId
    #########################################
    .state 'sheets.detail',
        url: ''
        views:
            'sheet-form':
                controller: 'SheetPartController as vm'
                template-url: '/static/templates/sheets/partials/sheet-form.html'
            'map-tabs':
                controller: 'MapTabsController as vm'
                template-url: '/static/templates/sheets/partials/map-tabs.html'
            'mct-segments-form':
                controller: 'SegmentCalculationsController as vm'
                template-url: '/static/templates/sheets/partials/mct-segments-form.html'
            'operations-grid':
                controller: 'SheetOperationGridController as vm'
                template-url: '/static/templates/sheets/partials/operations-grid.html'

]
