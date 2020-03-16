'use strict';

angular.module('mapping.auth.services')
.factory('AuthService', authService);

authService.$inject = ['$cookies', '$http', '$state', '$window', '$log', 'Toast', 'AUTHENTICATED'];

function authService($cookies, $http, $state, $window, $log, Toast, AUTHENTICATED) {
  return new class Auth {
    /**
     * User login
     * @memberof mapping.auth.services.AuthService
     * @param {string} email
     * @param {string} password
     */
    login(email, password) {
      $http.post('/api/v1/auth/login', {
        email: email,
        password: password
      })
      .then((result) => {
        // $log.debug('logged in as', result.data);
        // Toast.show(result.data);
        this.setAuthenticatedUser(result.data);
        Toast.show('Successfully logged in');
        // $state.go 'parts.index'
        // @todo use $state for redirection
        $window.location.href = '/parts';
      }, (result) => {
        Toast.error(result.data.message);
      });
    }

    /**
     * user logout
     */
    logout() {
      $http.post('/api/v1/auth/logout')
      .then((result) => {
        this.deauthenticate();
        Toast.show('Logging out...');
        $window.location = '/';
      }, (result) => {
        Toast.error(result.data.message);
      });
    }

    /**
     * Register new user
     * @param {string} email
     * @param {string} password
     */
    register(email, password) {
      $http.$post('/api/v1/users', {
        email: email,
        password: password
      });
    }

    /**
     * Retrieve the currently authenticated user
     */
    getAuthenticatedUser() {
      if (angular.isUndefined($cookies.get('user'))) {
        return;
      }
      return angular.fromJson($cookies.get('user'));
    }

    /**
     * Determine current authentication status
     *
     * WARNING: Do not use this for any security purposes. This is only used
     *          to display the correct login/logout link.
     *
     * @returns {boolean}
     */
    // isAuthenticated() { return !!$cookies.get('user') }
    // isAuthenticated() { return !!$cookies.get('sessionid') }
    isAuthenticated() { return AUTHENTICATED }

    /**
     * Set a cookie for the current user
     * @param {string} user
     */
    // setAuthenticatedUser(user) { $cookies.put('user', angular.toJson(user)) }
    // setAuthenticatedUser(user) { $cookies.put('user', angular.toJson(user), { expires: new Date(), secure: true }) }
    // setAuthenticatedUser(user) { $cookies.put('user', angular.toJson(user), { expires: (new Date()) }) }
    // setAuthenticatedUser(user) { $cookies.put('user', angular.toJson(user), { secure: true }) }
    setAuthenticatedUser(user) { const n = new Date(); $cookies.put('user', angular.toJson(user), { expires: new Date(n.getFullYear()-1, n.getMonth(), n.getDate()) }) }

    /**
     * Remove authentication cookie
     */
    deauthenticate() { $cookies.remove('user') }
  };
}
