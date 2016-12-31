/**
 * Created by jordan on 12/24/16.
 */
(function () {
    'use strict';
        angular.module('sample_1')
            .directive('sample1Author', AuthorDirective);
    function AuthorDirective(){
        return {
            templateUrl: '/static/html/author.html',
            restrict: 'E',
            controller: ['$scope', '$http', function ($scope, $http) {
                var url = '/sample_1/authors/' + $scope.author.id + '/';
                $scope.update = function () {
                    $http.put(url,$scope.author);
                };
                $scope.delete = function () {
                    $http.delete(url).then(function () {
                        var authors = $scope.authors;
                        authors.splice(
                            authors.indexOf($scope.author), 1
                        );
                    });
                };
                $scope.modelOptions = {
                    debounce: 500
                };
            }]
        };
    }
})();