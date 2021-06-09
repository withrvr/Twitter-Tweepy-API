let ctx = document.getElementById("usersChart").getContext("2d");
let myChart = new Chart(ctx, {
	type: "bar",
	data: {
		labels: users_found,
		datasets: [
			{
				label: "Followers",
				data: users_followers,
				backgroundColor: "rgba(255, 99, 132, 0.2)",
				borderColor: "rgba(255, 99, 132, 1)",
				borderWidth: 1,
			},
			{
				label: "Following",
				data: users_following,
				backgroundColor: "rgba(54, 162, 235, 0.2)",
				borderColor: "rgba(54, 162, 235, 1)",				
				borderWidth: 1,
			},
			{
				label: "Total Tweets",
				data: users_total_tweets,
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
		},
	},
});
