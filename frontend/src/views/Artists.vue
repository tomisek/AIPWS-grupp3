<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-8 ">
        
        <input @change="getListOfSongs" @keydown ="getListOfArtists" v-model="artist" class="form-control" list="datalistOptions" id="exampleDataList" placeholder="Enter name of artist here ..." autocomplete="off">
        <datalist id="datalistOptions">
        </datalist>

      </div>

      <div class="col-md-4 text-left artist-and-songs">
        <h3 class="artist-name"> Artist: {{ artist }}</h3>
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
        

    },
    methods:{

        async getListOfArtists(event){
          
          // Commentary:
          // At first this function was triggered by a keyup event. This lead to an extremely annoying flickering due to the
          // virtual DOM that was reusing previous searches to optmize speed. When the key was pressed down one could only
          // see the saved searches, if even for a short while. It looked like a bug in the app. I tried to find a way to override
          // this particular optimization, but I did not manage to get anywhere. Since the keydown event was causing all problems
          // I then choose it as the trigger for the function. Problem was that then I didn't have instant access to the latest 
          // added character in the input. So I had to do some uggly hacking.
          // I REALLY hope there is a smoother and a correct way to do this. /Konstantin

          
          $("#datalistOptions").empty()

          // hide the artist and songs whenever you're editing the input
          $(".artist-and-songs").css("visibility", "hidden")

          
          let artist = this.artist

          // No need to access the latest key value if it is any of these:
          if (event.which !== null && event.key !== 'Control' && event.key !== 'Alt'  && event.key !== 'ArrowLeft' && event.key !== 'ArrowRight' && event.key !== 'Enter' && event.key !== 'Shift') {
            let id = $(".form-control")[0].selectionStart
            artist = artist.slice(0, id) + event.key + artist.slice(id, artist.length)
          }
          
          // Code to make backspace and delete possible. 
          const regex5 = /%20Backspace/ig;
          artist = artist.replaceAll(regex5,"")
          const regex6 = /Delete%20/ig;
          artist = artist.replaceAll(regex6,"")
          const regex1 = /\s\SBackspace/ig;
          artist = artist.replaceAll(regex1,"")
          const regex2 = /.?Backspace/ig;
          artist = artist.replaceAll(regex2,"")
          const regex3 = /Delete.?/ig;
          artist = artist.replaceAll(regex3,"")


          // Ensure there will be no adding to a dropdown when the input is empty or when
          // an artist has been selected. When you click on an option, then apperantly it
          // counts as a key-event and the value is null.
          if (artist == '') {
            return
          }

          // Whenever a select is done, then 'event.which = null'. It can't replace the change
          // event for various reasons, but it will work fine for this little css-edit. Could not put
          // the following under a 'change-event' generated function, because if you search 
          // for the same thing twice, then the change-event will not fire up and therefore stay 
          // invisible.
          if (event.which == null){
            $(".artist-and-songs").css("visibility", "visible")
          }

          artist = artist.replaceAll("%20"," ")
          // When the string is sent by url, and it has a leading empty space, it will be cut off.
          // Therefore, we add it here
          if(artist[artist.length - 1] == " ") {
            artist = artist.substring(0, artist.length -1) + "%20"
          }
          console.log(artist)
          console.log(encodeURI(artist))
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


      },

      async getListOfSongs (){

        $("#listOfSongs").children().remove()
        
        let songs = await fetch(`/api/songs/${this.artist}`)
        songs = await songs.json()
        console.log(songs)
        for (let song of songs){
          this.songs.push(song)
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

  .artist-and-songs {
    visibility: hidden;
  }


</style>