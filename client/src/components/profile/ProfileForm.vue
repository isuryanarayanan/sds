<template>
  <div class="profile text-left p-5">
    <div class="profile-greet">
      <v-row>
        <v-col class="text-center">
          <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
          <v-file-input
            :rules="rules"
            accept="image/png, image/jpeg, image/bmp"
            placeholder="Pick an avatar"
            prepend-icon="mdi-camera"
            label="Avatar"
          ></v-file-input>
        </v-col>
        <v-col>
          <h1 class="font1">
            {{ $store.getters["user/get_user"]._USERNAME }}
          </h1>
          <h5 class="font2">{{ $store.getters["user/get_user"]._EMAIL }}</h5>
          <p class="font2 py-5">
            {{ $store.getters["user/get_user"]._BIO }} Lorem ipsum dolor sit
            amet consectetur adipisicing elit. Eaque consectetur atque veniam
            incidunt error saepe nostrum quaerat minima laborum, eius aliquam
            eos corrupti! Deleniti quae perferendis quis officia at quia.
          </p>
          <v-btn class="primary" small>Edit your profile</v-btn>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
export default {
  name: "Profile",
};
</script>
