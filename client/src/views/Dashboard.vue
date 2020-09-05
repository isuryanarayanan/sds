<template>
  <div class="dashboard text-left p-2">
    <div class="dashboard-greet">
      <h1 class="display-4 font2">
        Hey {{ $store.getters["user/get_user"]._USERNAME }}
      </h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
};
</script>
