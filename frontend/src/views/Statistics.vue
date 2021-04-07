<template>
  <main>
      <Buttons />
      <router-view />

  </main>
</template>
<script>
import Buttons from '../components/Buttons.vue'
import Viewstat from './Viewstat.vue'

export default {

  name: 'Statistics',

  components: {
    Buttons,
    Viewstat
  }

}
</script>

<style>

</style>