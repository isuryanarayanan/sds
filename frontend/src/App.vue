<template>
  <div id="app">
    <div id="nav" class="navbar bg-light font2">
      <div class="navbar-brand">
        Social Distancing Scheduler
      </div>
      <div class="navbar-links">
        <router-link to="/">Home</router-link> |
        <router-link to="/get-started">Get Started</router-link> |
        <router-link to="/about">About</router-link>
      </div>
    </div>
    <router-view />
  </div>
</template>
<script>
export default {
  data: () => {
    return {};
  },

  mounted: function() {
    // this.$store.dispatch("config/FORCE_AUTHENTICATE_USER");
  },
};
</script>
<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Francois+One&display=swap");
// font-family: 'Francois One', sans-serif;
@import url("https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap");
// font-family: 'Josefin Sans', sans-serif;
.font1 {
  font-family: "Francois One", sans-serif;
}
.font2 {
  font-family: "Josefin Sans", sans-serif;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
