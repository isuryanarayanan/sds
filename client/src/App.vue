<template>
  <v-app>
    <!-- Navigation bar -->
    <v-app-bar flat max-height="55px">
      <v-title class="font2">
        <strong>Social Distancing Scheduler</strong>
      </v-title>
      <v-spacer></v-spacer>
      <div class="font2">
        <!-- For the un authenticated user -->
        <div id="nav" v-if="$store.getters['user/get_authenticated'] == false">
          <router-link class="px-2" to="/">Home</router-link> |
          <router-link class="px-2" to="/get-started">Get Started</router-link>
        </div>
        <!-- For the authenticated user -->
        <div id="nav" v-if="$store.getters['user/get_authenticated'] == true">
          <router-link class="px-2" to="/dashboard">Dashboard</router-link> |
          <router-link class="px-2" to="/profile">Profile</router-link> |
          <router-link class="px-2" to="/logout">Logout</router-link>
        </div>
      </div>
    </v-app-bar>
    <!-- Navigation bar -->
    <!-- Router view -->
    <v-main>
      <router-view />
    </v-main>
    <!-- Router view -->
  </v-app>
</template>

<script>
export default {
  name: "App",
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
