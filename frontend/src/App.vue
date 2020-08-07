<template>
  <div id="app">
    <div id="nav" class="navbar bg-light font2">
      <div class="navbar-brand">
        Social Distancing Scheduler
        <div class="site-conf position-absolute">
          <div
            class="site-conf-btn btn btn-dark btn-sm"
            @click="ToggleSiteConf()"
          >
            Configuration {{ confSymbol }}
          </div>
          <div v-if="confView" class="">
            <div class="btn btn-primary btn-sm" @click="ForceAuthenticate()">
              Force Authenticate
            </div>
          </div>
        </div>
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
    return {
      confView: false,
      confSymbol: "+",
    };
  },
  methods: {
    ToggleSiteConf: function() {
      this.confView = !this.confView;
      if (this.confView == true) {
        this.confSymbol = "-";
      } else {
        this.confSymbol = "+";
      }
    },
    ForceAuthenticate: function() {
      this.$store.dispatch("config/FORCE_AUTHENTICATE");
      this.$router.push("/");
    },
  },
  mounted: function() {
    alert("app is mounted now check  permissions");
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
