/**
 * Created by jordan on 12/26/16.
 */
(function () {
    'use strict';
    angular.module('sample_1').run(['$http', run]);

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
})();