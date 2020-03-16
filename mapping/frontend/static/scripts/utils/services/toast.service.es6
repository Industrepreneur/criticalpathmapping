'use strict';

angular.module('mapping.utils.services')
.factory('Toast', toastService);

toastService.$inject = ['$mdToast', '$animate', '_'];

function toastService ($mdToast, $animate, _) {
  return new class Toast {
    /**
     * Display error feedback Toast message
     * @param {string} content - The content of the toast
     * @param {Object} options - Options to pass on to $mdToast
     * @memberof mapping.utils.services.Toast
     */
    error(content, options) { _toast(`Error: ${content}`, options) }

    /**
     * Display a standard Toast message
     * @param {string} content The content of the toast
     * @param {Object} options Options to pass on to $mdToast
     * @memberof mapping.utils.services.Toast
     */
    show(content, options) { _toast(content, options) }
  };


  /**
   * Display a toast
   * @param {string} content - The content of the toast
   * @param {Object} options - Options to pass on to $mdToast
   */
  function _toast(content, options) {
    options = _.extend({
      position: 'top left',
      template: `<md-toast>${content}</md-toast>`
    }, options);
    $mdToast.show(options);
  }
}
