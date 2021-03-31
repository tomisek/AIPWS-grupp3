<template>
  <div>
    <Prediction />

    <p>Popularity: {{ prediction }} </p>
  </div>
  
</template>

<script>
import Prediction from './components/Prediction.vue'

export default {
  name: 'App',
  components: {
    Prediction
  },
  computed: {
    prediction(){
      return this.$store.state.prediction
    }
  }
}
</script>
