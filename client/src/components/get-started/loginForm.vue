<template>
  <div class="py-3">
    <div class="li-brand font1">
      Login to an existing account
    </div>
    <div class="li-form">
      <form>
        <div class="form-group px-3">
          <label for="li-email">Email address</label>
          <input
            type="email"
            class="form-control"
            id="li-email"
            aria-describedby="emailHelp"
            placeholder=""
          />
        </div>
        <div class="form-group px-3">
          <label for="li-password1">Password</label>
          <input
            type="password"
            class="form-control"
            id="li-password1"
            placeholder=""
          />
        </div>

        <div class="p-3">
          <div class="form-group form-check">
            <input
              type="checkbox"
              class="form-check-input"
              id="li-cache-login"
            />
            <label class="form-check-label" for="li-cache-login"
              >Keep me signed in</label
            >
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
export default {
  name: "LoginForm",
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
