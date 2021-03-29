<template>
  <h3>Predicting spotify popularity</h3>
</template>

<script>
export default {
    methods:{
        async predict(){
            let values = {
                artists: 6316.0,
                acousticness : 0.678,
                year: 2020 
            }

            let res = await fetch('api/predict', {
                method: 'POST',
                body: JSON.stringify(values)
            })

            let prediction = await res.json()

            console.log(prediction)
        }
    },

    created(){
        this.predict()
    }
}
</script>

<style scoped>

</style>