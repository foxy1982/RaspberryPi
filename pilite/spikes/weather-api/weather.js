var request = require('request'),
 	_ = require('underscore');

request.get('https://api.forecast.io/forecast/c2e8234912c1eb9e429da907bcf84047/53.4667,2.2333', function(error, response, body) {
	if (error !== null) {
		return console.log('error');
	}

	var minutePeriod = 300;
	var hourPeriod = 14400;
	var period = minutePeriod;

	var minuteData = JSON.parse(body).minutely.data;
	var firstTime = minuteData[0].time;

	var data = _.map(minuteData, function (item) {
		return { time: item.time - firstTime, precipProbability: item.precipProbability };
	})

	data = _.groupBy(data, function(item) {
		return Math.floor(item.time / period);
	})

	data = _.map(data, function(item) {
		return _.reduce(item, function(memo, item) {
			return memo + item.precipProbability;
		}, 0) / item.length;
	})

	console.log(data);
});