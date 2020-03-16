'use strict';

angular.module('mapping.accounts.filters')
.filter('workPeriod', workPeriodFilter);

workPeriodFilter.$inject = ['_', 'WorkPeriodsService'];

function workPeriodFilter(_, WorkPeriods) {
  let hash = {};

  WorkPeriods.all()
  .then((t) => { _.each(t, (n) => { hash[n.id] = n.name }) });

  return function (input) { return input ? hash[input] : '' };
}
