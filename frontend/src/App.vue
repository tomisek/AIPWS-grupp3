<template>
  <p>
    <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Hello Vue 3.0 + Vite" />
    <Prediction />
  </p>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Prediction from './components/Prediction.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Prediction
  }
}
</script>
