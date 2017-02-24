/**
 * Created by jordan on 12/22/16.
 */
(function () {
    'use strict';
        angular.module('sample_1',["isteven-multi-select"])
            /*.factory('OptionsService', ['$http', function($http) {
                var Options = [];
            return {
                    $http.get('/sample_1/authors/').then(function (response) {
                        var arrayLength = response.data.length;
                        for (var i = 0; i < arrayLength; i++) {
                            Options.push(response.data[i].name);
                        }
                    });
                }
            };
        }])*/
        .controller('Sample_1_Controller', ['$scope', '$http', sample_1_Controller]);

        function sample_1_Controller($scope, $http) {
            $scope.login = function () {
                $http.post('/auth_sample_1/login/',
                    {username: $scope.user.username, password: $scope.user.password}
                )
            };

            $scope.authors = [];
            $http.get('/sample_1/authors/').then(function (response) {
                $scope.authors = response.data;
            });

            $scope.add_author = function (authors, n, d, e, p) {
                var author = {
                    name: n,
                    dni: d,
                    email: e,
                    phone: p
                };
                
                $http.post('/sample_1/authors/', author)
                    .then(function (response) {
                        authors.push(response.data)
                }, function (response) {
                        console.log(response.message);
                    });
            };
            /*Books*/
            $scope.books = [];
            $scope.addBookAuthors = [];
            $http.get('/sample_1/books/').then(function (response) {
                $scope.books = response.data;
                /*for(var i = 0, len = $scope.books.length; i < len; i++) {
                    if($scope.books[i].authors!=0)
                        $scope.sAuthors($scope.books[i].authors);
                }*/
            });
            /*$scope.sAuthors = function (authors) {
                for(var i = 0, len = authors.length; i < len; i++) {
                    authors[i].ticked = true;
                }
            };*/
            $scope.add_book= function (books, n, d, i, y) {
                var book = {
                    name: n,
                    description: d,
                    isbn: i,
                    year: y,
                    authors: []
                };
                angular.forEach($scope.addBookAuthors, function( value, key ) {
                    book.authors.push(value);
                });
                $http.post('/sample_1/books/', book)
                    .then(function (response) {
                        books.push(response.data)
                }, function (response) {
                        console.log(response.message);
                    });
            };
        }
})();
