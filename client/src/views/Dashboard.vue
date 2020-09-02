<template>
  <div class="dashboard text-left p-2">
    <div class="dashboard-greet">
      <h1 class="display-1 font2">
        Hey {{ $store.getters["user/get_username"] }}
      </h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
};
</script>
