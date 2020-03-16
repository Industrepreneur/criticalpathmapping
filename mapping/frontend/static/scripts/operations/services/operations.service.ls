'use strict'

angular.module 'mapping.operations.services'
    .factory 'OperationsService', operations-service

operations-service.$inject = <[ $log Restangular ]>
function operations-service ($log, Restangular)
    return new class Operations
        /**
         * Operations Service
         * @constructor
         * @memberof mapping.operations.services.OperationsService
         */
        -> @operations = void


        /**
         * Create a new Operation
         * @memberof mapping.operations.services.OperationsService
         ^ @param {object} newOperation - JSON object containing new Sheet data
         * @returns {Promise}
         */
        create: (new-operation) ->
            # $log.debug 'create-new-op', new-operation
            Restangular.all \operations
                .post new-operation
                /*.then (operation) ~> @operations.push operation; operation*/


        /**
         * Retrieve all Operations for the specified Sheet
         * @memberof mapping.operations.services.OperationsService
         * @param {number} sheetId - The id of the sheet to filter by
         * @returns {Promise}
         */
        for-sheet: (sheet-id) ->
            Restangular.one \sheets, sheet-id
                .all \operations
                .get-list!
                .then (operations) ~>
                    @operations = operations
                    operations
