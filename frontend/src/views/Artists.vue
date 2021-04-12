<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-8 ">
        
        <input @keyup.prevent ="getListOfArtists" v-model="artist" class="form-control" list="datalistOptions" id="exampleDataList" placeholder="Enter name of artist here ..." autocomplete="off">
        <datalist id="datalistOptions">
        </datalist>

        <p>Sort songs by</p>
        <div class="input-group mb-3">
          <select class="form-select" id="inputGroupSelect02">
            <option selected>Popularity</option>
            <option value="1">One</option>
          </select>
        </div>

      </div>

      <div class="col-md-4 text-left">
        <h3> Artist: {{ artist }}</h3>
        <ol id="listOfSongs">
          <li v-for="(s, index) of songs" :key="index" :song="s"  >
            {{s.name}} 
          </li>
        </ol>
        
      
      </div>

    </div>
  </div>

</template>

<script>
export default {

    data(){
        return{
            artist: '',
            songs: [],
        }
    },
      mounted(){
        // this.getListOfSongs()
      },
    methods:{

        async getListOfArtists(event){
            
                    
            let artist = this.artist

            
            let res = await fetch(`/api/artists/${artist}`)

            let listOfArtists = await res.json()
            let artistList = []
            for (let art of listOfArtists) {
              artistList.push(art.artists)
            }

            


            if (artist == '' || event.which == null) {
              $("#datalistOptions").empty()
              return;
            }
          
            $("#datalistOptions").empty()
            for (let ar of artistList) {
              ar = ar.replaceAll('"', '&quot;')
              $("#datalistOptions").append(`<option value=${'"' + ar + '"'}></option>`)
            }

            if ($("#form-control").val() == null){
              console.log("form-control")
              this.getListOfSongs()
            }
            // this.getListOfSongs()


        },

        async getListOfSongs (){

         
         let songs = await fetch(`/api/songs/${this.artist}`)


          songs = await songs.json()
          for (let song of songs){
            this.songs.push(song)
            console.log(song);
          }
        }
    }
}
</script>
 
<style scoped>
  p {
    text-align: left;
    margin-bottom: 2px;
    margin-top: 40px;
  }

  .form-control {
    width: 50%;
  }
  
</style>