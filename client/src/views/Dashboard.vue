<template>
  <div class="dashboard text-left p-5">
    <div class="dashboard-greet">
      <h1 class="font1">Hey {{ $store.getters["user/get_user"]._USERNAME }}</h1>
      <h5 class="font2">Welcome to your dashboard.</h5>
    </div>
    <v-tabs dark>
      <v-tab>Scheduler</v-tab>
    </v-tabs>
    <v-tabs-items>
      <v-tab-item>
        <v-card color="basil" flat>
          <v-card-text>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam
            corrupti impedit debitis aliquam, reprehenderit corporis sunt
            voluptatem eos sed dolore adipisci suscipit perferendis, deserunt
            est molestiae veniam exercitationem repellendus excepturi.
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
};
</script>
