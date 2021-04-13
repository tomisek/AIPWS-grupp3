<template>
  <div class="container-md">
    <canvas id="viewstatChart"></canvas>
  </div>
</template>

<script>  
export default {
  name : 'Viewstat',
  data() {
    return {
      canvas: "",
      chart: "",
      singing: [],
      popularity: []      
    }
  },

  mounted(){ 
    let canvas = document.getElementById('viewstatChart')
    let ctx = canvas.getContext('2d')
    this.canvas = ctx
    this.createChart()
    
  },
  methods: {   
    async createChart(){  
      await this.importSongs()
      this.chart = new Chart(this.canvas, {
        
        type: "bar",

        // The data for our dataset
        data: {
          labels: 
                this.singing
          ,
          datasets: [
            {
              label: "Max popularity by year from 1992-2007",//heading
              backgroundColor: ['red','blue','pink','orange','green'], //css colours'
              borderWidth: 2,
              borderColor: 'white',
              data: this.popularity,
              order: 0
            },
          ],
        },

        options: {  
          scales:{
            yAxes:[
              {
                tics:{
                  stepSize: 90000
                }
              }
            ]
          } 
        },
      
      });
    
    },
   
    async importSongs() {
      
      let songs = await fetch('/api/songs')
      songs = await songs.json(songs)
      console.log(songs)
      
        for(var i=0; i < songs.length; i++){
        
        this.singing.push(songs[i].year + songs[i].artists + "-" + songs[i].name)
        this.popularity.push(songs[i].max_popularity)
      }
      console.log(this.singing,this.popularity)      
    },       
  }
}
</script>