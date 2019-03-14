var ctx = document.getElementById("battery");

var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["0","1 Hour","2 Hours","3 Hours","4 Hours","5 Hours","6 hours","7 Hours"],
    datasets: [{
      label: "Sessions",
      lineTension: 0.3,
      backgroundColor: "rgba(2,117,216,0.2)",
      borderColor: "rgba(2,117,216,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(2,117,216,1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,117,216,1)",
      pointHitRadius: 20,
      pointBorderWidth: 2,
      data: [100,87,77,65,59,44,35,0]
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'Time'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 100
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});