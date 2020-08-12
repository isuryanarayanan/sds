<template>
  <div class="register-form py-3">
    <div class="su-brand font1">
      Create a new account
    </div>
    <div class="su-form">
      <form>
        <div class="form-group px-3">
          <label for="su-username">Username</label>
          <input
            type="text"
            class="form-control"
            id="su-username"
            aria-describedby="usernameHelp"
            placeholder="eg, JohnDoe"
          />
          <small id="usernameHelp" class="form-text text-muted"
            >Username should be unique</small
          >
        </div>
        <div class="form-group px-3">
          <label for="su-email">Email address</label>
          <input
            type="email"
            class="form-control"
            id="su-email"
            aria-describedby="emailHelp"
            placeholder="eg, johndoe@gmail.com"
          />
          <small id="emailHelp" class="form-text text-muted"
            >We'll never share your email with anyone else.</small
          >
        </div>
        <div class="form-group px-3">
          <label for="su-password1">Password</label>
          <input
            type="password"
            class="form-control"
            id="su-password1"
            placeholder=""
          />
          <ul>
            <li>
              <small id="usernameHelp" class="form-text text-muted"
                >Should contain atleast 8 characters</small
              >
            </li>
            <li>
              <small id="usernameHelp" class="form-text text-success"
                >Should contain atleast 1 uppercase character</small
              >
            </li>
            <li>
              <small id="usernameHelp" class="form-text text-muted"
                >Should contain atleast 1 numeral</small
              >
            </li>
          </ul>
        </div>
        <div class="form-group px-3">
          <label for="su-password2">Password Confirmation</label>
          <input type="password" class="form-control" id="su-password2" />
        </div>
        <div class="p-3">
          <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="su-agreement" />
            <label class="form-check-label" for="su-agreement"
              >Accept terms and conditions,
              <span class="text-primary">read.</span></label
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
  name: "RegisterForm",
};
</script>
<style lang="scss" scoped>
.signup {
  :hover .su-brand {
    color: #42b983;
  }
}

.su-brand {
  font-size: 32px;
  color: #2c3e50;
}
</style>
