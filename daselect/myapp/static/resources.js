angular.module('main')

    .config(['$resourceProvider', function ($resourceProvider) {
        // Don't strip trailing slashes from calculated URLs
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }])

    .factory('Child', ['$resource', function ($resource) {
        return $resource('/api/children/:pk/', {'pk': '@pk'}, {'update': {'method': 'PUT'}});
    }]);
