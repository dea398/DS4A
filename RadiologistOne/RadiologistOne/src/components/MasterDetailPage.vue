<template>
  <div class="col">
    <div class="row heading">
      <div class="col">
        <div id="dwv">
          <div class="layerContainer">
            <carousel-3d
              ref="mycarousel"
              :controls-visible="true"
              :clickable="true"
              :perspective="0"
              :inverse-scaling="1500"
              :space="700"
              :width="200"
              :height="200"
            >
              <slide :index="0">
                <figure id="dwv0" style="width: 100%;">
                  <div class="layerContainer">
                    <canvas class="imageLayer" style="width: 100%;"></canvas>
                  </div>
                  <figcaption>Patient 1</figcaption>
                </figure>
              </slide>
              <slide :index="1">
                <figure id="dwv1">
                  <div class="layerContainer">
                    <canvas class="imageLayer" style="width: 100%;"></canvas>
                  </div>
                  <figcaption>Patient 2</figcaption>
                </figure>
              </slide>
              <slide :index="2">
                <figure id="dwv2" style="width: 100%;">
                  <div class="layerContainer">
                    <canvas class="imageLayer" style="width: 100%;"></canvas>
                  </div>
                  <figcaption>Patient 3</figcaption>
                </figure>
              </slide>
            </carousel-3d>
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
      containerDivId: "dwv0",
      fitToWindow: "true",
      tools: ["Scroll"]
    });
    var i;
    var list0 = [];
    for (i = 0; i < 4; i++) {
      list0[i] = "Patient1/T1_TSE_TRA/T1_TSE_TRA__0001_00" + (i + 1) + ".dcm";
    }
    app0.loadURLs(list0);

    // create the second dwv app
    var app1 = new dwv.App();
    // initialise with the id of the container div
    app1.init({
      containerDivId: "dwv1",
      fitToWindow: "true",
      tools: ["Scroll"]
    });

    var j;
    var list1 = [];
    for (j = 0; j < 5; j++) {
      list1[j] = "Patient2/T1_TSE_TRA/T1_TSE_TRA__0002_00" + (j + 1) + ".dcm";
    }
    // load dicom data
    app1.loadURLs(list1);

    // create the third dwv app
    var app2 = new dwv.App();
    app2.init({
      containerDivId: "dwv2",
      fitToWindow: "true",
      tools: ["Scroll"]
    });

    var k;
    var list2 = [];
    for (k = 0; k < 5; k++) {
      list2[k] = "Patient3/T1_TSE_TRA/T1_TSE_TRA__0003_00" + (k + 1) + ".dcm";
    }

    app2.loadURLs(list2);
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
  background-color: black;
  padding-top: 2em;
  padding-bottom: 0em;
}
.imageLayer {
  width: 15rem;
}
</style>
