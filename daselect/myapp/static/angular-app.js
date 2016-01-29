angular.module('main', [
    'ng', 'ngResource', 'ng.django.forms'
]);


mainController = function ($scope, Child) {
	Child.get({pk:2}).$promise.then(function (ch) {
		$scope.dj_child = ch;
	});
};
mainController.$inject = ['$scope', 'Child'];

angular.module('main').controller('mainController', mainController);
