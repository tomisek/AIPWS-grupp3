<template>

  <div class="row">
    <div class="col">
      
      <input @keyup.prevent ="getListOfArtists" v-model="artist" class="form-control" list="datalistOptions" id="exampleDataList" placeholder="Enter name of artist here ..." autocomplete="off">
      <datalist id="datalistOptions">
        <option value="Taylor Swift"></option>
      </datalist>

      <!-- <input @keyup.prevent ="getListOfArtists" v-model="artist" class ="artList" type="text" list="myList">
      <datalist id="myList">
        <option value="Taylor Swift"></option>
      <!-- </datalist> -->

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
        async getListOfArtists(){

            let artist = this.artist
            
            let res = await fetch(`/api/artists/${artist}`)

            let listOfArtists = await res.json()
            let artistList = []
            for (let art of listOfArtists) {
              artistList.push(art.artists)
            }

            console.log(listOfArtists)
            $("#datalistOptions").empty()
            for (let ar of artistList) {
              console.log(ar)
              $("#datalistOptions").append(`<option value=${ar}></option>`)
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