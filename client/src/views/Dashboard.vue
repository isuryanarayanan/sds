<template>
  <div class="dashboard text-left p-5">
    <div class="dashboard-greet">
      <h1 class="font1">Hey {{ $store.getters["user/get_user"]._USERNAME }}</h1>
      <h5 class="font2">Welcome to your dashboard.</h5>
    </div>
    <v-tabs dark>
      <v-tab>Dashboard</v-tab>
      <v-tab-item>
        <calendar />
      </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
import calendar from "../components/Calendar/calendarComponent.vue";
export default {
  name: "Dashboard",
  components: {
    calendar,
  },
  data() {
    return {
      tabs: null,
    };
  },
};
</script>
