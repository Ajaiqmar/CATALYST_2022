'use strict';
const catalyst = require("zcatalyst-sdk-node");

module.exports = (req, res) => {
	var url = req.url.split("?",2)[0];

	const app = catalyst.initialize(req);

	switch (url) {
		case '/analyzeSentiment':
			const zia = app.zia();
			var tweet = req.url.split("?",2)[1].split("=",2)[1];

			zia.getSentimentAnalysis([tweet])
			.then((result) => {
				result = JSON.stringify(result)
				res.send(result);
				res.end();
			})
			.catch((error) => {
				res.send(error.toString());
				res.end();
			});

			break;
		case '/reportOperator':
			var username = req.url.split("?",2)[1].split("&",2)[0].split("=",2)[1];
			var tweet = req.url.split("?",2)[1].split("&",2)[1].split("=",2)[1];

			const config = {
				from_email: "knowledge232002@gmail.com",
				to_email: ["ajaiqmar@gmail.com"],
				subject: "URGENT!! Issue raised by the customer.",
				content: "<h1>"+username+"</h1><br/><h1>"+tweet+"</h1>"
			};

			const email = app.email();

			email.sendMail(config).then((mailObject) => {
				mailObject = JSON.stringify(mailObject)
				res.send(mailObject);
				res.end();
    	}).catch((err) => {
				res.send(err.toString());
				res.end();
			});

			break;
		default:
			res.writeHead(404);
			res.write('You might find the page you are looking for at "/" path');
			res.end();
			break;
	}
};
