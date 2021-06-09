let ctx = document.getElementById("tweetsChart").getContext("2d");
let myChart = new Chart(ctx, {
	type: "bar",
	data: {
		labels: tweets_found,
		datasets: [
			{
				label: "Likes",
				data: tweets_likes,
				backgroundColor: "rgba(54, 162, 235, 0.2)",
				borderColor: "rgba(54, 162, 235, 1)",
				borderWidth: 1,
			},
			{
				label: "Retweets",
				data: tweets_retweets,
				backgroundColor: "rgba(255, 206, 86, 0.2)",
				borderColor: "rgba(255, 206, 86, 1)",
				borderWidth: 1,
			},
		],
	},
	options: {
		scales: {
			y: {
				beginAtZero: true,
			},			
			x: {
				ticks: {
					autoSkip: false,
					maxRotation: 90,
					minRotation: 90,
				},
			},
		},
	},
});
