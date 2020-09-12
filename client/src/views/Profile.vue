<template>
  <div class="profile p-5">
    <v-card>
      <v-row>
        <v-col class="col-sm-8">
          <div class="text-left px-5">
            <div class="profile-greet">
              <h1 class="font1">
                Hey {{ $store.getters["user/get_user"]._USERNAME }}
              </h1>
              <p class="font2 primary--text">
                You can manage your profile here.
              </p>
              <h5 class="font2">
                {{ $store.getters["user/get_user"]._EMAIL }}
              </h5>
            </div>
          </div>
        </v-col>
        <v-col class="col-sm-4">
          <div class="edit px-5">
            <v-btn>Edit your profile <v-icon small>fas fa-edit</v-icon></v-btn>
          </div>
        </v-col>
      </v-row>
    </v-card>
    <!--
    	<v-title class="display-1 p-2">
      		{{ $store.getters["user/get_user"]._USERNAME }}
    	</v-title>

    	<v-btn>Edit<v-icon small>fas fa-edit</v-icon></v-btn>
    	<v-title class="display-1 p-2">
     		{{ $store.getters["user/get_user"]._EMAIL }}
    	</v-title>

    	<v-btn>Edit<v-icon small>fas fa-edit</v-icon></v-btn>
    	-->
  </div>
</template>

<script>
export default {
  name: "Profile",
};
</script>
