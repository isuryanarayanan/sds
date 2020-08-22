<template>
  <div id="app">
    <div class="navbar font2">
      <!-- Branding -->
      <div class="navbar-brand">
        Social Distancing Scheduler
      </div>
      <div class="navbar-links">
        <!-- For the un authenticated user -->
        <div id="nav" v-if="$store.getters['user/get_authenticated'] == false">
          <router-link to="/">Home</router-link> |
          <router-link to="/get-started">Get Started</router-link>
        </div>
        <!-- For the authenticated user -->
        <div id="nav" v-if="$store.getters['user/get_authenticated'] == true">
          <router-link to="/dashboard">Dashboard</router-link> |
          <router-link to="/profile">Profile</router-link> |
          <router-link to="/logout">Logout</router-link>
        </div>
      </div>
    </div>
    <!-- The router view -->
    <router-view />
  </div>
</template>
<script>
export default {
  mounted: function() {
    this.$store.dispatch("load");
    if (this.$store.getters["user/get_authenticated"]) {
      this.$router.push({ name: "Dashboard" });
    } else {
      console.log("unauthenticated");
    }
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
