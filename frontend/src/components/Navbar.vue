<template>
<main>
  <div class="jumbotron jumbotron-fluid" style="background-color: #20c997;">

      <router-link class="text-dark" to="/"><h1>Spotify song popularity</h1></router-link>
      
    <nav class="navbar navbar-expand-sm navbar-light bg-lightm " style="background-color: #20c997;">
      <div class="container-fluid">
        
          <div class="navbar-nav mx-auto">
            <ul class="navbar-nav">
              <li class="nav-item">
                <router-link class="nav-link" to="/predict">Predict</router-link>
              </li>

                <li class="nav-item">
                  <router-link class="nav-link" to="/statistics">Statistics</router-link>
                </li>
            </ul>
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