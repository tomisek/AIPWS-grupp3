<template>
    <form @submit.prevent ="predict">
      <h3>Predicting spotify popularity</h3>
      <input v-model="artists" type="range" name="artist" placeholder="artist" min="1" max="30000" >
      <label for="artist">Artist</label><br>
      <input v-model="acousticness" type="range" name="acousticness" placeholder="acousticness" min="0" max="1"  step="0.001">
      <label for="acousticness">Acousticness</label><br>
      <input v-model="year" type="range" name="year" placeholder="year" min="1920" max="2021" >
      <label for="year">Year</label><br>
      <button>test</button>
  </form>
</template>

<script>
export default {
    data(){
        return{
            artists: 15000,
            acousticness: 0.5,
            year: 1970
        }
    },
    methods:{
        async predict(){
            
            
            let values = {
                artists: this.artists,
                acousticness : this.acousticness,
                year: this.year
            }

            let res = await fetch('api/predict', {
                method: 'POST',
                body: JSON.stringify(values)
            })

            let prediction = await res.json()

            this.$store.commit('setPrediction', prediction)

            console.log(prediction)
        }
    },

    created(){
    
    }
}
</script>

<style scoped>

</style>