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
        <p class="title">Healthcare Provider</p>
        <p>{{ textSampleData.shipFrom }}</p>
        <p class="title">Age</p>
        <p>{{ textSampleData.age }}</p>
        <div id="myDIV" v-show="textSampleData.probability > 0">
          <p class="title">Classification</p>
          <p>{{ textSampleData.status }}</p>
          <p class="title">Probability</p>
          <p>{{ textSampleData.probability }}</p>
        </div>
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
    textSampleData: {
      type: Object,
      required: true,
      validator: function(value) {
        return (
          value.id !== undefined &&
          value.longDescription !== undefined &&
          value.shortDescription !== undefined &&
          value.orderDate !== undefined &&
          value.age !== undefined &&
          value.shipFrom !== undefined &&
          value.status !== undefined &&
          value.probability !== undefined &&
          value.name !== undefined
        );
      }
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
