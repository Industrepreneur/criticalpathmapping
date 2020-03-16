'use strict';

/**
 * HTML5 autofocus polyfill directive
 */
angular.module('mapping.utils.directives')
.directive('autofocus', autofocusDirective);

autofocusDirective.$inject = ['$document', '$timeout'];

function autofocusDirective ($document, $timeout) {
  return {
    link: function ($scope, $element) {
      $timeout((() => { $element[0].focus() }), 500);
    }
  };
}
