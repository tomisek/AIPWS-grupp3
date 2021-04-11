<template>

  <div class="row">
    <div class="col">
      
      <input v-on:keydown ="getListOfArtists" v-model="artist" class="form-control" list="datalistOptions" id="exampleDataList" placeholder="Enter name of artist here ..." autocomplete="off">
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

    <div class="col">
      <ol>
        <li>Song1</li>
        <li>Song2</li>
        <li>Song3</li>
        <li>Song4</li>
        <li>Song5</li>
        <li>Song6</li>
        <li>Song7</li>
        <li>Song8</li>
        <li>Song9</li>
        <li>Song10</li>
      </ol>
    </div>

  </div>

</template>

<script>

export default {
    data(){
        return{
            artist: ''
        }
    },
    methods:{

        async getListOfArtists(event){
          // Commentary:
          // At first this function was triggered by a keyup event. This lead to an extremely annoying flickering due to the
          // virtual DOM that was reusing previous searches to optmize speed. When the key was pressed down one could only
          // see the saved searches, if even for a short while. It looked like a bug in the app. I tried to find a way to override
          // this particular optimization, but I did not manage to get anywhere. Since the keydown event was causing all problems
          // I then choose it as the trigger for the function. Problem was that then I didn't have instant access to the latest 
          // added character in the input. So I had to do some uggly hacking. In the end you cannot use the mouse pointer to position 
          // yourself in the middle of the word if you want correct dropdown results. I choose to save this version simply because I 
          // put a lot of time on this and it is really a question of what you rather not have. I hate flickering.
          // I REALLY hope there is a smoother and a correct way to do this. /Konstantin
            
            $("#datalistOptions").empty()
            let artist = this.artist

            // Unless we're using the delete key, we're assuming that the inserted
            // key should be at the end of the word.
            // No need to access the latest key value if it is any of these three:
            if (event.key !== 'Control' && event.key !== 'Alt' && event.which !== 32) {
              artist = artist + event.key
            }
            // Can only use delete when positioned at the start.
            else if (event.key == 'Delete') {
              artist = event.key + artist  
            }

            // The space bar key (code 32) seems to be trimmed of when send with fetch function below,
            // so we do the following hack:
            artist = (event.which == 32 ? artist + "%20": artist) 

            // Code to make backspace and delete possible. 
            // Can only use backspace when positioned at the end.
            // Can only use delete when positioned at the start.
            const regex1 = /\s\SBackspace/ig;
            artist = artist.replaceAll(regex1,"%20")
            const regex2 = /.?Backspace/ig;
            artist = artist.replaceAll(regex2,"")
            const regex3 = /Delete.?/ig;
            artist = artist.replaceAll(regex3,"")
            const regex4 = /Delete\S\s/ig;
            artist = artist.replaceAll(regex4,"%20")


            let res = await fetch(`/api/artists/${artist}`)


            let listOfArtists = await res.json()
            let artistList = []
            for (let art of listOfArtists) {
              artistList.push(art.artists)
            }

            

            // Ensure there will be no adding to a dropdown when the input is empty or when
            // an artist has been selected. When you click on an option, then apperantly it
            // counts as a key-event and the value is null.
            if (artist == '' || event.which == null) {
              return
            }
          
            for (let ar of artistList) {
              ar = ar.replaceAll('"', '&quot;')
              $("#datalistOptions").append(`<option value=${'"' + ar + '"'}></option>`)
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