'use strict';

angular.module('mapping.operations.filters')
.filter('operationMethod', operationMethodFilter);

operationMethodFilter.$inject = ['_', 'OperationMethodsService'];

function operationMethodFilter(_, OperationMethods) {
  let hash = {};

  OperationMethods.all()
  .then((t) => { _.each(t, (n) => { hash[n.id] = n.name }) });

  return function (input) { return input ? hash[input] : '' };
}
