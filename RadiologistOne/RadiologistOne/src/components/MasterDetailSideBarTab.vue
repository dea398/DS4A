<template>
  <v-expansion-panels :focusable="true" :inset="true" :multiple="false">
    <v-expansion-panel>
      <v-expansion-panel-header>
        <button
          class="list-group-item list-group-item-action styles.sidebarText"
          type="button"
          @click="$emit('onDisplayTabClick', index)"
        >
          <v-avatar>
            <img
              class="mr-3"
              style="width:30px; height:30px"
              src="patient.png"
            />
          </v-avatar>
          {{ tabText }}
        </button>
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
export default {
  name: "MasterDetailSideBarTab",
  props: {
    tabText: {
      type: String,
      required: true
    },
    index: {
      type: Number,
      required: true
    }
  }
};
</script>

<style scoped>
.sidebarText {
  font-weight: 500;
}
</style>
