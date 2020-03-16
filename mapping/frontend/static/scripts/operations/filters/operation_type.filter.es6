'use strict';

angular.module('mapping.operations.filters')
.filter('operationType', operationTypeFilter);

operationTypeFilter.$inject = ['_', 'OperationTypesService'];

function operationTypeFilter(_, OperationTypes) {
  let hash = {};

  OperationTypes.all()
  .then((t) => { _.each(t, (n) => { hash[n.id] = n.name }) });

  return function (input) { return input ? hash[input] : '' };
}
