angular.module('main', [
    'ng', 'ngResource', 'ng.django.forms'
]);


mainController = function ($scope, Child, Parent) {
	Parent.query().$promise.then(function (parents) {
		$scope.parents = parents;
		Child.get({pk:2}).$promise.then(function (ch) {
			$scope.dj_child = ch;
			console.log($scope.dj_child);
		});
		console.log($scope.parents);
	});
};
mainController.$inject = ['$scope', 'Child', 'Parent'];

angular.module('main').controller('mainController', mainController);
