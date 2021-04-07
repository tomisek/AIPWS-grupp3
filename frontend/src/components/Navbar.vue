<template>
<main>
  <div class="jumbotron jumbotron-fluid" style="background-color: #20c997;">
    <!-- <div class="page-header" > -->
      <router-link class="text-dark" to="/"><h1>Spotify song popularity</h1></router-link>
      
    <!-- </div> -->
    <nav class="navbar navbar-expand-sm navbar-light bg-lightm " style="background-color: #20c997;">
      <div class="container-fluid">
        <!-- <a class="navbar-brand" href="#">Navbar</a> -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav mx-auto">
            <!-- <router-link class="nav-link " aria-current="page" to="/">Home</router-link> -->
            <router-link class="nav-link" to="/predict">Predict</router-link>
            <router-link class="nav-link" to="/statistics">Statistics</router-link>
            
          </div>
        </div>
      </div>
    </nav>
  </div>
</main>
  
</template>

<script>
export default {

}
</script>

<style scoped>
.router-link-active{
  background:rgba(43, 49, 30, 0.11);
}
h1 {
  font-family: 'Julius Sans One', sans-serif;
}

</style>