<template>
  <div class="dashboard text-left p-2">
    <div class="dashboard-greet">
      <h1 class="display-4 font1">
        Hey {{ $store.getters["user/get_user"]._USERNAME }}
      </h1>
      <h5 class="font2">{{ $store.getters["user/get_user"]._EMAIL }}</h5>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dashboard"
};
</script>
