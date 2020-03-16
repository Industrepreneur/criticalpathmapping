'use strict';

angular.module('mapping.operations.filters')
.filter('valueTypeStyle', valueTypeStyleFilter);

valueTypeStyleFilter.$inject = ['VALUE_TYPES'];

function valueTypeStyleFilter(VALUE_TYPES) {
  let hash = {
    [VALUE_TYPES.VALUE_ADD]: {
      fill       : 'rgb(39, 174, 96)',
      is_striped : false
    },
    [VALUE_TYPES.NON_VALUE_ADD]: {
      fill       : 'rgb(240, 0, 7)',
      is_striped : false
    },
    [VALUE_TYPES.REQUIRED_NON_VALUE_ADD]: {
      fill       : 'rgb(243, 156, 18)',
      is_striped : false
    }
  };

  return function (input) { return hash[input] ? hash[input] : { fill: 'rgb(255, 0, 204)', is_striped: false } };
}
