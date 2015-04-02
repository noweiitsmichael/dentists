var default_options = {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: 0,
        plotShadow: false
    },
    title: {
    },
    subtitle: {
        useHTML: true,
        verticalAlign: 'middle',
        y: -20
    },
    plotOptions: {
        pie: {
            dataLabels: {
                enabled: false
            }
        }
    },
    series: [{
        type: 'pie',
        innerSize: '60%'
    }]
};    

function create_chart(container, title, subtitle, ys, colors) {
    var options = $.extend({}, default_options);
    options.title.text = title;
    options.subtitle.text = subtitle;
    var data = _(ys).zip(colors).map(function(x) {
        return { y: x[0], color: x[1] };
    }).value();        
    options.series[0].data = data;
    console.debug(options);
    container.highcharts(options);    
}

$(function () {
    create_chart($('#net_production'), 
                 'Net Production', 
                 '<h3>$48,879<br></h3>Goal: $38,533<br>Pace: $69,245', 
                 [48879-38533, 38533-(48879-38533)], 
                 ['#09B009', '#AAAAAA']);
    create_chart($('#collection'), 
                 'Collection', 
                 '<h3>$31,953<br></h3>Goal: $32,981<br>Pace: $45,267', 
                 [32981-(32981- 31953), 32981- 31953], 
                 ['#AAAAAA', '#AAAA00']);
    create_chart($('#reappoint_rate'), 
                 'Reappoint Rate', 
                 '<h3>82%<br></h3>Goal: 80%', 
                 [2, 80], 
                 ['#09B009', '#AAAAAA']);
    create_chart($('#new_patients'), 
                 'New Patients', 
                 '<h3>63<br></h3>Goal: 79<br>Pace: 89', 
                 [79-(79-63), 79-63], 
                 ['#AAAAAA', '#AAAA00']);      
    $('#key_procedures').highcharts({
        title: {
            text: 'Key Procedures, Megan'
        },
        xAxis: [{
            categories: ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
        }],
        yAxis: [{ // Primary yAxis
        }, { // Secondary yAxis
            opposite: true
        }],
        tooltip: {
            shared: true
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            x: 50,
            verticalAlign: 'top',
            y: 20,
            floating: true,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
        },
        series: [{
            name: 'Prophies',
            type: 'column',
            data: [91, 102, 101, 97, 94, 96, 104, 122, 105, 75, 93, 94]
        }, {
            name: '4910',
            type: 'line',
            yAxis: 1,
            color: '#AAAAAA',
            data: [20, 17, 14, 18, 26, 7, 14, 17, 15, 15, 16, 12]
        }, {
            name: 'Fluoride',
            type: 'line',
            yAxis: 1,
            color: '#1010C0',
            data: [7, 13, 6, 14, 13, 11, 17, 20, 13, 10, 11, 16]
        }, {
            name: 'SRP',
            type: 'line',
            yAxis: 1,
            color: '#000040',
            data: [12, 8, 6, 5, 5, 9, 7, 12, 9, 9, 6, 13]
        }]
    });    
});
