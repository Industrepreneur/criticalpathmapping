'use strict'

angular.module 'mapping.parts.services'
    .factory 'PartsService', parts-service

parts-service.$inject = <[ $log Restangular ]>
function parts-service ($log, Restangular)
    return new class Parts
        /**
         * Parts Service
         * @constructor
         * @memberof mapping.parts.services.PartsService
         */
        -> @parts = Restangular .all \parts .get-list!


        /**
         * @name all
         * @desc Get all Parts for the current users' Company
         * @memberof mapping.parts.services.PartsService
         * @returns {Promise}
         */
        all: -> @parts


        /**
         * Create a new Part
         * @memberof mapping.parts.services.PartsService
         ^ @param {object} JSON object containing new Part data
         * @returns {Promise}
         */
        create: (newPart) ->
            Restangular.all \parts
                .post newPart
                .then (part) ~> @parts.push part; return part


        /**
         * Get one Part by id
         * @memberof mapping.parts.services.PartsService
         * @param {int} id The unique Part ID
         * @returns {Promise}
         */
        one: (id) -> Restangular.one \parts id .get!


        /**
         * Delete a Part by id
         * @memberof mapping.parts.services.PartsService
         * @param {int} id The unique Part ID
         * @returns {Promise}
         */
        remove: (part) ->
            @parts.then (parts) ->
                id = _.find-key parts, {id: part}
                parts[id].remove! .finally ~> parts.splice id, 1
