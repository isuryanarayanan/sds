<template>
  <div class="py-3">
    <div class="li-brand font1">
      Login to an existing account
    </div>
    <div class="li-form">
      <div class="form-group px-3">
        <label for="li-email">Email address</label>
        <input
          type="email"
          class="form-control"
          id="li-email"
          aria-describedby="emailHelp"
          placeholder=""
          v-model="email"
        />
      </div>
      <div class="form-group px-3">
        <label for="li-password1">Password</label>
        <input
          type="password"
          class="form-control"
          id="li-password1"
          placeholder=""
          v-model="password"
        />
      </div>

      <div class="p-3">
        <div class="form-group form-check">
          <input type="checkbox" class="form-check-input" id="li-cache-login" />
          <label class="form-check-label" for="li-cache-login"
            >Keep me signed in</label
          >
        </div>
        <button class="btn btn-primary" @click="SubmitApi()">
          Submit
        </button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "LoginForm",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    SubmitApi: function() {
      this.$store.dispatch("user/GET_JWT_TOKEN", {
        username: this.email,
        password: this.password,
      });
      this.$router.replace("/");
    },
    Submit: function() {
      this.$store.dispatch("user/get_token", {
        email: this.email,
        password: this.password,
      });
      this.$router.replace("/dashboard");
    },
  },
};
</script>
<style lang="scss" scoped>
.login {
  :hover .li-brand {
    color: #42b983;
  }
}

.li-brand {
  font-size: 32px;
  color: #2c3e50;
}
</style>
