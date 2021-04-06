<template>
  <main>
    <Prediction />
    <p>Popularity: {{ prediction }} </p>

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