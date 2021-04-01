<template>
  <main>
    <Navbar />
    <router-view />
    <Prediction />
    <!-- <p>Popularity: {{ prediction }} </p> -->

  </main>
    
</template>

<script>
import Prediction from './components/Prediction.vue'
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Prediction,
    Navbar
  },
  computed: {
    prediction(){
      return this.$store.state.prediction
    }
  }
}
</script>
