<template>
  <div class="home">
    <div class="home-wrapper">
      <div class="brand p-5 text-center">
        <h1 class="display-1 font1">Social Distancing Scheduler</h1>
      </div>
      <div class="sub-brand text-center px-5">
        <p class="font2 px-5">
          Social Distancing Scheduler is a standard to schedule your contacts
          and avoid contracting viruses like COVID-19. Built using Python, with
          the Django framework for the backend and Vue js for the frontend. SDS
          allows its users to see how many people have registered to be present
          at a public space at a given time. SDS is not a product or service it
          is a standard.
        </p>
      </div>
      <div class="call-to-action text-center">
        <router-link to="/get-started" class="text-light px-1">
          <div class="btn btn-dark btn-lg shadow">Get Started</div>
        </router-link>
        <a
          href="https://github.com/devdoodan/social-distancing-scheduler"
          class="text-light px-1"
        >
          <div class="btn btn-secondary shadow">Contribute</div>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  components: {},
};
</script>

<style lang="scss" scoped>
.home-wrapper {
  width: 100%;
  .sub-brand {
    font-size: 24px;
  }
}
</style>
