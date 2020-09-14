<template>
  <div class="profile text-left p-5">
    <div class="profile-greet">
      <v-row>
        <v-col v-if="!showForm" class="text-center">
          <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
        </v-col>
        <v-col v-if="!showForm">
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
          <v-btn class="primary" small @click="OpenForm()" v-if="!showForm"
            >Edit your profile</v-btn
          >
        </v-col>
        <v-btn dark small @click="CloseForm()" v-if="showForm">Go Back</v-btn>
        <v-col v-if="showForm">
          <ProfileForm />
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import ProfileForm from "../components/profile/ProfileForm.vue";
export default {
  name: "Profile",
  components: {
    ProfileForm,
  },
  data: () => ({
    showForm: false,
  }),
  methods: {
    OpenForm: function() {
      this.showForm = true;
    },
    CloseForm: function() {
      this.showForm = false;
    },
  },
};
</script>

// {{ $store.getters["user/get_user"]._USERNAME }}
