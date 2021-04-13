<template>
  <main>
    <Prediction />
    <div class="container">
      <p>Popularity (0 - 100) as measured by Spotify: {{ prediction }} </p>

    </div>

  </main>
    
</template>

<script>
import Prediction from '../components/Prediction.vue'

export default {
  name: 'Predict',
  components: {
    Prediction,
  },
  computed: {
    prediction(){
      return this.$store.state.prediction
    }
  }
}
</script>