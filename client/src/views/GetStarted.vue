<template>
  <div class="get-started p-5">
    <div class="get-started-wrapper row">
      <div class="signup p-1 col-sm-6">
        <div class="py-3">
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
              </div>
              <div class="form-group px-3">
                <label for="su-password2">Password Confirmation</label>
                <input type="password" class="form-control" id="su-password2" />
              </div>
              <div class="p-3">
                <div class="form-group form-check">
                  <input
                    type="checkbox"
                    class="form-check-input"
                    id="su-agreement"
                  />
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
      </div>
      <div class="login p-1 col-sm-6">
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
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.signup {
  :hover .su-brand {
    color: #42b983;
  }
}
.login {
  :hover .li-brand {
    color: #42b983;
  }
}

.su-brand,
.li-brand {
  font-size: 32px;
  color: #2c3e50;
}
</style>
