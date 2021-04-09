<template>
  <main>
      <Buttons />
      <router-view />

  </main>
</template>
<script>
import Buttons from '../components/Buttons.vue'

export default {

  name: 'Statistics',

  components: {
    Buttons,
  }

}
</script>

<style>

</style>