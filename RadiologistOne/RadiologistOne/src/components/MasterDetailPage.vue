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
              :perspective="35"
              :inverse-scaling="1000"
              :space="700"
              :width="450"
              :height="400"
            >
              <slide :index="0">
                <figure id="dwv0" style="width: 100%;">
                  <div class="layerContainer">
                    <canvas class="imageLayer" style="width: 100%;"></canvas>
                  </div>
                  <figcaption>D3</figcaption>
                </figure>
              </slide>
              <slide :index="1">
                <figure id="dwv1">
                  <div class="layerContainer">
                    <canvas class="imageLayer" style="width: 100%;"></canvas>
                  </div>
                  <figcaption>D4</figcaption>
                </figure>
              </slide>
              <slide :index="2">
                <figure id="dwv2" style="width: 100%;">
                  <div class="layerContainer">
                    <canvas class="imageLayer" style="width: 100%;"></canvas>
                  </div>
                  <figcaption>D5</figcaption>
                </figure>
              </slide>
            </carousel-3d>
          </div>
          <span data-id="btnNext" @click="nextSlide()" style="display:none">
            <i class="fa fa-refresh"></i>
          </span>
          <h3 class="ml-3 mb-4">{{ textSampleData.name }}</h3>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-8 col-12 ml-3 mb-5">
        <p></p>
        <p class="title">Order Date</p>
        <p>{{ textSampleData.orderDate }}</p>
        <p class="title">Patient Description</p>
        <p>{{ textSampleData.shortDescription }}</p>
        <p class="title" v-show="textSampleData.probability > 0">Annotations</p>
        <p v-show="textSampleData.probability > 0">{{ textSampleData.longDescription }}</p>
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

    var list0 = [];
    for (var i = 0; i < 4; i++) {
      list0[i] =
        "Patient1/T1_TSE_TRA/D3/T1_TSE_TRA__0005_00" + (i + 1) + ".dcm";
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

    var list1 = [];
    for (i = 0; i < 4; i++) {
      if (i + 6 == 10) {
        list1[i] =
          "Patient1/T1_TSE_TRA/D4/T1_TSE_TRA__0005_0" + (i + 6) + ".dcm";
      } else {
        list1[i] =
          "Patient1/T1_TSE_TRA/D4/T1_TSE_TRA__0005_00" + (i + 6) + ".dcm";
      }
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

    var list2 = [];
    for (i = 0; i < 4; i++) {
      list2[i] =
        "Patient1/T1_TSE_TRA/D5/T1_TSE_TRA__0005_0" + (i + 11) + ".dcm";
    }

    app2.loadURLs(list2);

    var Leap = require("leapjs");
    const btnNext = document.querySelector('[data-id="btnNext"]');

    Leap.loop(function(frame) {
      if (frame.gestures.length > 0 && frame.id % 15 === 0) {
        btnNext.click();
      }
    });
  },
  methods: {
    nextSlide() {
      this.$refs.mycarousel.goNext();
    },
    prevSlide() {
      this.$refs.mycarousel.goPrev();
    }
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
  height: 500px;
  padding-top: 3em;
  padding-bottom: 0em;
}

.carousel-3d-slide {
  background-color: black;
}

.carousel-3d-container figcaption {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  color: #fff;
  bottom: 0;
  padding: 15px;
  font-size: 12px;
  min-width: 100%;
  box-sizing: border-box;
}
</style>
