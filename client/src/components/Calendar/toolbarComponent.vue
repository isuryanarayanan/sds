<template>
  <v-row class="fill-height">
    <v-col>
      <v-sheet>
        <v-toolbar flat>
          <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="$store.commit('set_today')"
          >
            Today
          </v-btn>
          <v-btn fab text small color="grey darken-2" @click="prev">
            <v-icon small>
              mdi-chevron-left
            </v-icon>
          </v-btn>
          <v-btn fab text small color="grey darken-2" @click="next">
            <v-icon small>
              mdi-chevron-right
            </v-icon>
          </v-btn>
          <v-toolbar-title v-if="refs">
            {{ refs["calendar"].title }}
          </v-toolbar-title>
          <v-spacer></v-spacer>
          <v-menu bottom right>
            <template v-slot:activator="{ on, attrs }">
              <v-btn outlined color="grey darken-2" v-bind="attrs" v-on="on">
                <span>{{ TypeToLabel }}</span>
                <v-icon right>
                  mdi-menu-down
                </v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item @click="set_type('day')">
                <v-list-item-title>Day</v-list-item-title>
              </v-list-item>
              <v-list-item @click="set_type('week')">
                <v-list-item-title>Week</v-list-item-title>
              </v-list-item>
              <v-list-item @click="set_type('month')">
                <v-list-item-title>Month</v-list-item-title>
              </v-list-item>
              <v-list-item @click="set_type('4day')">
                <v-list-item-title>4 days</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-toolbar>
      </v-sheet>
    </v-col>
  </v-row>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data() {
    return {};
  },
  computed: {
    ...mapGetters({ TypeToLabel: "get_typeToLabel", refs: "get_refs" }),
  },
  mounted() {},
  methods: {
    prev() {
      this.$emit("prev");
    },
    next() {
      this.$emit("next");
    },
    set_type(type) {
      this.$store.commit("set_type", type);
    },
  },
};
</script>

<style lang="scss" scoped></style>
