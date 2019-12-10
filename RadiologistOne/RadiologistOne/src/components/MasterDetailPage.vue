<template>
  <div class="col">
    <div class="row heading">
      <div class="col">
        <div id="dwv">
          <div class="layerContainer">
            <canvas class="imageLayer"></canvas>
          </div>
          <h3 class="ml-3 mb-4">{{ textSampleData.name }}</h3>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12 mt-3">
        <b-breadcrumb class="bg-white">
          <b-breadcrumb-item href="#">Master Detail</b-breadcrumb-item>
          <b-breadcrumb-item active>{{
            textSampleData.name
          }}</b-breadcrumb-item>
        </b-breadcrumb>
      </div>
      <div class="col-md-8 col-12 ml-3 mb-5">
        <p class="title">Patient</p>
        <p>{{ textSampleData.name }}</p>
        <p class="title">Order Date</p>
        <p>{{ textSampleData.orderDate }}</p>
        <p class="title">Healthcare Provider</p>
        <p>{{ textSampleData.shipFrom }}</p>
        <p class="title">Age</p>
        <p>{{ textSampleData.age }}</p>
        <p class="title">Description</p>
        <p>{{ textSampleData.shortDescription }}</p>
        <p class="title">Classification</p>
        <p>{{ textSampleData.status }}</p>
        <p class="title">Probability</p>
        <p>{{ textSampleData.probability }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import dwv from "dwv";
export default {
  name: "MasterDetailPage",
  props: {
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
    }
  },
  mounted() {
    // base function to get elements
    dwv.gui.getElement = dwv.gui.base.getElement;
    dwv.gui.displayProgress = function() {};
    // refresh element
    dwv.gui.refreshElement = dwv.gui.base.refreshElement;
    // create the first dwv app
    var app0 = new dwv.App();
    app0.init({
      containerDivId: "dwv",
      fitToWindow: "true",
      tools: ["Scroll"]
    });
    var i;
    var list0 = [];
    for (i = 0; i < 4; i++) {
      list0[i] = "Patient1/T1_TSE_TRA/T1_TSE_TRA__0001_00" + (i + 1) + ".dcm";
    }
    app0.loadURLs(list0);
  }
};
</script>

<style scoped>
.title {
  font-weight: 700;
  margin-bottom: 0;
}

.breadCrumbLink {
  color: #025fce;
}

.heading {
  background-color: #cecece;
  padding-top: 4em;
}
.imageLayer {
  width: 30rem;
}
</style>
