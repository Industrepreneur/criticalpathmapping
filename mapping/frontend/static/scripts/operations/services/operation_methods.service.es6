'use strict';

angular.module('mapping.operations.services')
.factory('OperationMethodsService', operationMethodsService);

operationMethodsService.$inject = ['Restangular'];

function operationMethodsService(Restangular) {
  return new class OperationMethods {
    /**
     * operationMethodsService
     * @constructor
     * @memberof mapping.operations.services.OperationMethods
     */
    constructor() {
      this.operationMethods = Restangular.all('operation_methods').getList();
    }

    /**
     * Get all Operation Methods
     * @memberof mapping.operations.services.OperationMethods
     * @returns {Promise}
     */
    all() { return this.operationMethods }
  };
}
