<template>
  <div class="profile p-5">
    <v-title class="display-1 p-2">
      {{ $store.getters["user/get_user"]._USERNAME }}</v-title
    >

    <v-btn>Edit<v-icon small>fas fa-edit</v-icon></v-btn>
    <v-title class="display-1 p-2">
      {{ $store.getters["user/get_user"]._EMAIL }}</v-title
    >

    <v-btn>Edit<v-icon small>fas fa-edit</v-icon></v-btn>
  </div>
</template>

<script>
export default {
  name: "Profile",
};
</script>
