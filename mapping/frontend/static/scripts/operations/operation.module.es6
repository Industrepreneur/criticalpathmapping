'use strict';

angular.module('mapping.operations', [
  'mapping.operations.filters',
  'mapping.operations.services'
])

.constant('OPERATION_TYPES', {
  OFF_HOURS: 10,
  INSPECTION_PIECE: 3,
  INSPECTION_BATCH: 4,
  OUTSIDE_PROCESSING: 7,
  PROCESSING_PIECE: 1,
  PROCESSING_BATCH: 2,
  REWORK: 6,
  SETUP: 5,
  WAIT_FOR_LOT: 9,
  WAIT_FOR_RESOURCE: 8
})

.constant('VALUE_TYPES', {
  VALUE_ADD: 'VA',
  NON_VALUE_ADD: 'NVA',
  REQUIRED_NON_VALUE_ADD: 'RNVA'
});

angular.module('mapping.operations.filters', []);

angular.module('mapping.operations.services', ['restangular']);
