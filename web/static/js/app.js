var app = angular.module('OfficeFileApp', []);

app.controller('OfficeFileController', function($scope, $http) {
    $scope.files = [];
    $scope.getAll =  function() {
        $http.get('/api/v1/officefile/').then(function(response) {
            $scope.files = response.data.objects;
        });
    };
    $scope.getAll();

    google.charts.load('current', {'packages':['corechart']});

    $scope.delete =  function(id) {
        $http.delete('/api/v1/officefile/'+ id + '/');
        $scope.getAll();
    };

    $scope.clickme = function (f) {
        var actualFile = JSON.parse(f.dict_coor);
        var array = [];
        console.log(actualFile);

        for (key in actualFile) {
            if (key == 'x_value') {
                var minX = actualFile.x_value[0];
                var maxX = actualFile.x_value[0];

                for(var i=0; i<actualFile.x_value.length; i++) {
                    array.push([actualFile.x_value[i], actualFile.y_value[i]]);

                    if(actualFile.x_value[i] > maxX){
                        actualFile.x_value[i] = maxX;
                    } else if (actualFile.x_value[i] < minX) {
                        actualFile.x_value[i] = minX;
                    }

                    if(actualFile.y_value[i] > maxX){
                        actualFile.y_value[i] = maxX;
                    } else if (actualFile.y_value[i] < minX) {
                        actualFile.y_value[i] = minX;
                    }
                }
            }

            if (key == 'x') {
                var minX = actualFile.x[0];
                var maxX = actualFile.x[0];

                for(var i=0; i<actualFile.x.length; i++) {
                    array.push([actualFile.x[i], actualFile.y[i]]);

                    if(actualFile.x[i] > maxX){
                        actualFile.x[i] = maxX;
                    } else if (actualFile.x[i] < minX) {
                        actualFile.x[i] = minX;
                    }

                    if(actualFile.y[i] > maxX){
                        actualFile.y[i] = maxX;
                    } else if (actualFile.y[i] < minX) {
                        actualFile.y[i] = minX;
                    }
                }
            }
        }



        google.charts.setOnLoadCallback(drawChart);
        function drawChart() {
            var data = new google.visualization.DataTable();
            data.addColumn('number', 'x');
            data.addColumn('number', 'y');
            data.addRows(array);

            var options = {
            title: 'Graphic:',
            hAxis: {title: 'y', minValue: minX-5, maxValue: maxX+5},
            vAxis: {title: 'x', minValue: minX-5, maxValue: maxX+5},
            legend: 'none'
            };

            var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));

            chart.draw(data, options);
        }
    };

});