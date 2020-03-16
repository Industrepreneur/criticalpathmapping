'use strict';

angular.module('mapping.parts.controllers')
.controller('PartsController', partsController);

partsController.$inject = ['$scope', '$state', 'AuthService', 'PartsService', 'parts'];
function partsController ($scope, $state, Auth, PartsService, parts) {
  let vm = this;
  vm.parts = parts;
  vm.isAuthenticated = Auth.isAuthenticated();
}
