<template>
    <main>

        <!-- <form @submit.prevent ="predict">
            <h3>Predicting spotify popularity</h3>
            <input v-model="artists" type="range" name="artist" placeholder="artist" min="1" max="30000" >
            <label for="artist">Artist</label><br>
            <input v-model="acousticness" type="range" name="acousticness" placeholder="acousticness" min="0" max="1"  step="0.001">
            <label for="acousticness">Acousticness</label><br>
            <input v-model="year" type="range" name="year" placeholder="year" min="1920" max="2021" >
            <label for="year">Year</label><br>
            <button>test</button>
        </form> -->
        <div class="container-md  ">
            <form @submit.prevent ="predict">
                <div class ="form-group row">
                    <label for="artist" class="col-sm-2 col-form-label text-left">Artist </label>
                    <input type="range" v-model="artists" placeholder="Enter artist name..." min="1" max="30000">
                </div>
                <div class="form-group row">
                    <label for="acousticness" class="col-sm-2 col-form-label text-left">Acousticness</label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ acousticness }}</div>
                    <input v-model="acousticness" type="range" class="form-control-range" id="acousticness" min="0" max="1"  step="0.001">
                </div>
                <div class="form-group row">
                    <label for="year" class="col-sm-2 col-form-label text-left">Year </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ year }}</div>
                    <input v-model="year"  type="range" class="form-control-range" id="year" min="1920" max="2021" >
                </div>
                <fieldset class="form-group row float-left">
                    <legend class="col-form-label col-sm-2 pt-0">Explicit</legend>
                    <div class="col-sm-10">
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios1" value="option1" checked>
                        <label class="form-check-label" for="gridRadios1">
                        No
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios2" value="option2">
                        <label class="form-check-label" for="gridRadios2">
                        Yes
                        </label>
                    </div>
                    </div>
                </fieldset>

                <div class="form-group row">
                    <div class="col-sm-10">
                    <button type="submit" class="btn btn-primary">test</button>
                    </div>
                </div>

            </form>
        </div>
    </main>
</template>

<script>
export default {
    data(){
        return{
            artists: "",
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