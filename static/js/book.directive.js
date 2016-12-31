/**
 * Created by jordan on 12/27/16.
 */
(function () {
    'use strict';
        angular.module('sample_1')
            .directive('sample1Book', BookDirective);
    function BookDirective(){
        return {
            templateUrl: '/static/html/book.html',
            restrict: 'E',
            controller: ['$scope', '$http', function ($scope, $http) {
                var url = '/sample_1/books/' + $scope.book.id + '/';
                //$scope.opc2 = $scope.book.authors;
                $scope.updateBookAuthors = [];
                $scope.update = function () {
                    $scope.book.authors = $scope.updateBookAuthors;
                    $http.put(url, $scope.book);
                };
                $scope.delete = function () {
                    $http.delete(url).then(function () {
                        var books = $scope.books;
                        books.splice(
                            books.indexOf($scope.book), 1
                        );
                    });
                };
                $scope.modelOptions = {
                    debounce: 500
                };
                /*$scope.setAuthors = function () {
                    angular.forEach($scope.book.authors, function( value, key ) {
                    console.log(value);
                    //book.authors.push(value);
                });
                }*/
            }]
        };
    }
})();