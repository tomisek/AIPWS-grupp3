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
          console.log(event.which)
          // Commentary:
          // At first this function was triggered by a keyup event. This lead to an extremely annoying flickering due to the
          // virtual DOM that was reusing previous searches to optmize speed. When the key was pressed down one could only
          // see the saved searches, if even for a short while. It looked like a bug in the app. I tried to find a way to override
          // this particular optimization, but I did not manage to get anywhere. Since the keydown event was causing all problems
          // I then choose it as the trigger for the function. Problem was that then I didn't have instant access to the latest 
          // added character in the input. So I had to do some uggly hacking. In the end it is kind of working. The only bug is:
          // when you move the cursor with any of the arrow-keys, then you have to click on the drop-down-arrow to see the options.
          // I REALLY hope there is a smoother and a correct way to do this. /Konstantin

            $("#datalistOptions").empty()
            let artist = this.artist

            // No need to access the latest key value if it is any of these:
            if (event.key !== 'Control' && event.key !== 'Alt'  && event.key !== 'ArrowLeft' && event.key !== 'ArrowRight' && event.key !== 'Enter' && event.key !== 'Shift') {
              let id = $(".form-control")[0].selectionStart
              artist = artist.slice(0, id) + event.key + artist.slice(id, artist.length)
            }

            // The space bar key (code 32) seems to be trimmed of when send with fetch function below,
            // so we do the following hack:
            artist = artist.replaceAll(" ", "%20")

            // Code to make backspace and delete possible. 
            // Can only use backspace when positioned at the end.
            // Can only use delete when positioned at the start.
            const regex5 = /%20Backspace/ig;
            artist = artist.replaceAll(regex5,"")
            const regex6 = /Delete%20/ig;
            artist = artist.replaceAll(regex6,"")
            const regex1 = /\s\SBackspace/ig;
            artist = artist.replaceAll(regex1,"%20")
            const regex2 = /.?Backspace/ig;
            artist = artist.replaceAll(regex2,"")
            const regex3 = /Delete.?/ig;
            artist = artist.replaceAll(regex3,"")
            const regex4 = /Delete\S\s/ig;
            artist = artist.replaceAll(regex4,"%20")

            // Ensure there will be no adding to a dropdown when the input is empty or when
            // an artist has been selected. When you click on an option, then apperantly it
            // counts as a key-event and the value is null.
            if (artist == '' || event.which == null) {
              return
            }
            console.log(artist)
            let res = await fetch(`/api/artists/${artist}`)


            let listOfArtists = await res.json()
            let artistList = []
            for (let art of listOfArtists) {
              artistList.push(art.artists)
            }

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