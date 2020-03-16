'use strict';

angular.module('mapping.operations.filters')
.filter('operationTypeStyle', operationTypeStyleFilter);

operationTypeStyleFilter.$inject = ['$log', '_', 'OperationTypesService', 'OPERATION_TYPES'];

function operationTypeStyleFilter($log, _, OperationTypes, OPERATION_TYPES) {
  let hash = {
    [OPERATION_TYPES.SETUP]: {
      fill       : 'rgb(243, 156, 18)',
      is_striped : false
    },
    [OPERATION_TYPES.PROCESSING_BATCH]: {
      fill       : 'rgb(39, 175, 96)',
      is_striped : false
    },
    [OPERATION_TYPES.PROCESSING_PIECE]: {
      fill       : 'rgb(39, 175, 96)',
      is_striped : false
    },
    [OPERATION_TYPES.WAIT_FOR_RESOURCE]: {
      fill       : 'rgb(240, 0, 7)',
      is_striped : false
    },
    [OPERATION_TYPES.WAIT_FOR_LOT]: {
      fill       : 'rgb(240, 0, 7)',
      is_striped : true
    },
    [OPERATION_TYPES.OUTSIDE_PROCESSING]: {
      fill       : 'rgb(243, 156, 18)',
      is_striped : true
    },
    [OPERATION_TYPES.INSPECTION_BATCH]: {
      fill       : 'rgb(215, 138, 8)',
      is_striped : false
    },
    [OPERATION_TYPES.INSPECTION_PIECE]: {
      fill       : 'rgb(215, 138, 8)',
      is_striped : false
    },
    [OPERATION_TYPES.OFF_HOURS]: {
      fill       : 'rgb(194, 26, 0)',
      is_striped : false
    },
    [OPERATION_TYPES.REWORK]: {
      fill       : 'rgb(211, 84, 0)',
      is_striped : false
    },
  };

  return function (input) { return hash[input] ? hash[input] : { fill: 'rgb(255, 0, 204)', is_striped: false } };
}
