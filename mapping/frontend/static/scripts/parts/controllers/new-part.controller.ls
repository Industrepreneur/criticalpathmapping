'use strict'

angular.module 'mapping.parts.controllers'
    .controller 'NewPartController', new-part-controller

new-part-controller.$inject = <[ $rootScope $scope $mdDialog $log Toast PartsService ]>
!function new-part-controller ($rootScope, $scope, $mdDialog, $log, Toast, Parts)
    vm = this

    /**
     * Reset form and close modal dialog
     * @memberof mapping.parts.controllers.NewPartController
     */
    cancel = -> $mdDialog.hide!
    vm.cancel = cancel

    /**
     * Create a new Part
     * @memberof mapping.parts.controllers.NewPartController
     */
    submit = ->
        part =
            name: vm.name
            description: vm.description

        Parts.create(part).then createPartSuccessFn, createPartErrorFn
    vm.submit = submit

    function createPartSuccessFn (data, status, headers, config)
        part = data
        $rootScope.$broadcast 'part.created', part
        Toast.show "Added new part - #{part.name}"
        $mdDialog.hide!

    function createPartErrorFn (data, status, headers, config)
        $rootScope.$broadcast 'part.created.error'
        Toast.error data.name.0
