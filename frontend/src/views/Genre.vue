<template>
  <div class ="container">
    <h2>Hello from Genre.vue</h2>
    <canvas id="genreChart"></canvas>
  </div>

</template>

<script>


export default {
  data() {
    return {
      canvas: '',

      
    }
  },

  mounted(){
    let canvas = document.getElementById('genreChart')
    let ctx = canvas.getContext('2d')
    this.canvas = ctx
    this.createChart()
  },
  methods: {
    createChart(){
      this.chart = new Chart(this.canvas, {
        // The type of chart we want to create
        type: "line",

        // The data for our dataset
        data: {
          labels: [
            "Red",
            "Blue",
            "Green",
          ],
          datasets: [
            {
              label: "Dataset",
              backgroundColor: ['red', 'blue', 'green'],
              borderWidth: 2,
              borderColor: [],
              data: [30, 15, 20 ],
              order: 0
            },
          ],
        },
      });
    }
  }
}
</script>
