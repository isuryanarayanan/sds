<template>
  <div class="dashboard text-left p-5">
    <div class="dashboard-greet">
      <h1 class="font1">Hey {{ $store.getters["user/get_user"]._USERNAME }}</h1>
      <h5 class="font2">Welcome to your dashboard.</h5>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
};
</script>
