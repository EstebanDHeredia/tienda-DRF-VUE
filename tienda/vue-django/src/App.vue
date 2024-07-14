<template>
  <div class="container">

    <navbar-component></navbar-component>

    <navigation-component></navigation-component>

    <router-view/>

    <footer-component></footer-component>

  </div>



</template>

<script>

import FooterComponent from "./components/FooterComponent"
import NavbarComponent from "./components/NavbarComponent"
import NavigationComponent from "./components/NavigationComponent"

export default {
  name: 'App',

  components: {
    FooterComponent,
    NavbarComponent,
    NavigationComponent
  }

}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
