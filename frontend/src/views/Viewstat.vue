<template>
  <div class="container">
    <canvas id="viewstatChart"></canvas>
    <h2>Most popular songs by year from 1992 - 2007 (most popular years in all time)</h2>
  </div>

</template>

<script>  

// import Chart from 'chart.js'

export default {
  name : 'Viewstat',
  data() {
    return {
      canvas: '',

      
    }
  },

  mounted(){
    let canvas = document.getElementById('viewstatChart')
    let ctx = canvas.getContext('2d')
    this.canvas = ctx
    this.createChart()
  },
  methods: {
    createChart(){
      this.chart = new Chart(this.canvas, {
        // The type of chart we want to create
        type: "bar",

        // The data for our dataset
        data: {
          labels: [
            "1992 Rage Against The Machine - Killing in the name",//x-axel strings
            "1993 Radiohead - Creep",
            "1994 Mariah Carey - All I want for Christmass is you",
            "1995 Coolio', 'L.V.' - Gangsta's Paradise	",
            "1996 Spice Girls - Wannabe",
            "1997 The Verve - Bitter Sweet Symphony	",
            "1998 George Michael - Careless Whisper	",
            "1999 Red Hot Chili Peppers - Californication",
            "2000 Coldplay - Yellow",
            "2001 Pappa Roach - Last Resort",
            "2002 Eminem', Nate Dogg - Till I Collapse",
            "2003 Linkin Park - Numb",
            "2004 Usher, Lil Jon, Ludacris - Yeah!",
            "2005 Shakira, Wyclef Jean - Hips Don't Lie",
            "2006 Nelly Furtado, Timbaland - Promiscuous",
            "2007 Kanye West - Stronger"

          ],
          datasets: [
            {
              label: "Dataset",//heading
              backgroundColor: ['red', 'blue', 'green','yellow','pink'], //css colours
              borderWidth: 2,
              borderColor: 'white',
              data: [78, 80, 90, 81, 79, 78, 78, 80, 85, 80, 83, 81, 81, 82, 81, 80 ],
              order: 0
            },
          ],
        },
        // Configuration options go here
        options: {
          // onClick(e){
          //   // console.log(this.chart.getElementAtEvent(e))
          //   let point = this.chart.getElementAtEvent(e)[0]
          //   console.log(point)
          //   if(point){
          //     let label = this.chart.data.labels[point._index]
          //     let value = this.chart.data.datasets[point._datasetIndex].data[point._index]
          //     console.log(label, value)
          //    }
          // }
        },
      });
    }
  }
}
</script>