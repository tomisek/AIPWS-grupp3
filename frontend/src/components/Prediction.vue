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
        <div class="container-md ">
            <form @submit.prevent ="predict">
                <div class ="form-group row">
                    <label for="artist" class="col-sm-2 col-form-label text-left">Artist </label>
                    <input type="text" v-model="artists" placeholder="Enter artist name...">
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

                <fieldset class="form-group row">
                    <legend class="col-form-label col-sm-2 text-left">Explicit</legend>
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
                    <label for="danceability" class="col-sm-2 col-form-label text-left">Danceability </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ danceability }}</div>
                    <input v-model="danceability"  type="range" class="form-control-range" id="danceability" min="0" max="1" step="0.001" >
                </div>

                <div class="form-group row">
                    <label for="energy" class="col-sm-2 col-form-label text-left">Energy </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ energy }}</div>
                    <input v-model="energy"  type="range" class="form-control-range" id="energy" min="0" max="1" step="0.001" >
                </div>
                
                <div class="form-group row">
                    <label for="instrumentalness" class="col-sm-2 col-form-label text-left">Instrumentalness </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ instrumentalness }}</div>
                    <input v-model="instrumentalness"  type="range" class="form-control-range" id="instrumentalness" min="0" max="1" step="0.001" >
                </div>

                <div class="form-group row">
                    <label for="key" class="col-sm-2 col-form-label text-left"> Key </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ key }}</div>
                    <input v-model="key"  type="range" class="form-control-range" id="key" min="0" max="11">
                </div>

                <div class="form-group row">
                    <label for="liveness" class="col-sm-2 col-form-label text-left">Liveness </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ liveness }}</div>
                    <input v-model="liveness"  type="range" class="form-control-range" id="liveness" min="0" max="1" step="0.001" >
                </div>

                <div class="form-group row">
                    <label for="speechiness" class="col-sm-2 col-form-label text-left">Speechiness </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ speechiness }}</div>
                    <input v-model="speechiness"  type="range" class="form-control-range" id="speechiness" min="0" max="1" step="0.001" >
                </div>

                <div class="form-group row">
                    <label for="valence" class="col-sm-2 col-form-label text-left">Valence </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ valence }}</div>
                    <input v-model="valence"  type="range" class="form-control-range" id="valence" min="0" max="1" step="0.001" >
                </div>

                <div class="form-group row">
                    <label for="tempo" class="col-sm-2 col-form-label text-left">Tempo </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ tempo }}</div>
                    <input v-model="tempo"  type="range" class="form-control-range" id="tempo" min="0" max="243" >
                </div>

                <div class="form-group row">
                    <label for="loudness" class="col-sm-2 col-form-label text-left">Loudness </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ loudness }}</div>
                    <input v-model="loudness"  type="range" class="form-control-range" id="loudness" min="-55" max="3">
                </div>

                <div class="form-group row">
                    <label for="duration" class="col-sm-2 col-form-label text-left">Duration (ms) </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ duration_ms }}</div>
                    <input v-model="duration_ms"  type="range" class="form-control-range" id="duration" min="4.937000e+03" max="5.338302e+06" step="0.001" >
                </div>

                <div class="form-group row">
                    <label for="release_date_month" class="col-sm-2 col-form-label text-left">Release date month</label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ release_date_month }}</div>
                    <input v-model="release_date_month"  type="range" class="form-control-range" id="release_date_month" min="1" max="12">
                </div>

                <div class="form-group row">
                    <label for="release_date_day" class="col-sm-2 col-form-label text-left">Release date day </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ release_date_day }}</div>
                    <input v-model="release_date_day"  type="range" class="form-control-range" id="release_date_day" min="1" max="31">
                </div>

                <div class="form-group row">
                    <label for="release_date_dayofweek" class="col-sm-2 col-form-label text-left">Release date dayofweek <br> 0=Monday 6=Sunday </label>
                    <div class="form-group row col-sm-2 col-form-label"> {{ release_date_dayofweek }}</div>
                    <input v-model="release_date_dayofweek"  type="range" class="form-control-range" id="release_date_dayofweek" min="0" max="6">
                </div>

                

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
            // mean values
            artists: 13896.0,
            acousticness: 0.501345,
            year: 1976,
            danceability: 0.536404,
            energy: 0.481353,
            explicit: 0.067844,
            instrumentalness: 0.194523,
            key: 5.205564,
            liveness: 0.211400,
            speechiness: 0.105972,
            valence: 0.525459,
            tempo: 116.963254,
            loudness: -11.76946,
            duration_ms: 2.326434e+05,
            release_date_month: 4.331701,
            release_date_day: 8.227629,
            release_date_dayofweek: 2.688245
        }
    },
    methods:{
        async predict(){
            
            
            let values = {
                artists: this.artists,
                acousticness : this.acousticness,
                year: this.year,
                danceability: this.danceability,
                energy: this.energy,
                explicit: this.explicit,
                instrumentalness: this.instrumentalness,
                key: this.key,
                liveness: this.liveness,
                speechiness: this.speechiness,
                valence: this.valence,
                tempo: this.tempo,
                loudness: this.loudness,
                duration_ms: this.duration_ms,
                release_date_month: this.release_date_month,
                release_date_day: this.release_date_day,
                release_date_dayofweek: this.release_date_dayofweek
            }

            let res = await fetch('api/predict', {
                method: 'POST',
                body: JSON.stringify(values)
            })

            let prediction = await res.json()

            this.$store.commit('setPrediction', prediction)

            console.log(prediction[0])
            console.log(values.year)
            console.log(values.artists)
        }
    },

    created(){
    
    }
}
</script>

<style scoped>

</style>