'use strict';

angular.module('mapping.operations.services')
.factory('OperationTypesService', operationTypesService);

operationTypesService.$inject = ['Restangular'];

function operationTypesService (Restangular) {
  return new class OperationTypes {
    /**
     * PartsService
     * @constructor
     * @memberof mapping.operations.services.OperationTypes
     */
    constructor() {
      this.operationTypes = Restangular.all('operation_types').getList();
    }

    /**
     * Get all Operation Types
     * @memberof mapping.operations.services.OperationTypes
     * @returns {Promise}
     */
    all() { return this.operationTypes }
  };
}
