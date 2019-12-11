<template>
  <div class="mainDiv">
    <carousel-3d
      ref="mycarousel"
      :controls-visible="true"
      :clickable="true"
      :perspective="0"
      :inverse-scaling="1500"
      :space="800"
      :width="550"
      :height="500"
    >
      <slide :index="0">
        <figure id="dwv0" style="width: 100%;">
          <div class="layerContainer">
            <canvas class="imageLayer" style="width: 100%;"></canvas>
          </div>
          <!--<input type="range" id="sliceRange" value="0" /> -->
          <figcaption>T1 TSE D3</figcaption>
        </figure>
      </slide>
      <slide :index="1">
        <figure id="dwv1">
          <div class="layerContainer">
            <canvas class="imageLayer" style="width: 100%;"></canvas>
          </div>
          <!--<input type="range" id="sliceRange" value="0" /> -->
          <figcaption>T1 TSE D4</figcaption>
        </figure>
      </slide>
      <slide :index="2">
        <figure id="dwv2" style="width: 100%;">
          <div class="layerContainer">
            <canvas class="imageLayer" style="width: 100%;"></canvas>
          </div>
          <!--<input type="range" id="sliceRange" value="0" /> -->
          <figcaption>T1 TSE D5</figcaption>
        </figure>
      </slide>
      <slide :index="3">
        <figure id="dwv3" style="width: 100%;">
          <div class="layerContainer">
            <canvas class="imageLayer" style="width: 100%;"></canvas>
          </div>
          <!--<input type="range" id="sliceRange" value="0" /> -->
          <figcaption>T1 TSE SAG</figcaption>
        </figure>
      </slide>
      <slide :index="4">
        <figure id="dwv4" style="width: 100%;">
          <div class="layerContainer">
            <canvas class="imageLayer" style="width: 100%;"></canvas>
          </div>
          <!--<input type="range" id="sliceRange" value="0" /> -->
          <figcaption>T2 TSE SAG</figcaption>
        </figure>
      </slide>

      <!--
      <slide v-for="(slide, i) in slides" :key="i" :index="i">
        <dwvVue style="width: 100%; height:500px;" />
        
        <figure>
          <img src="https://www.spineuniverse.com/sites/default/files/imagecache/gallery-large/wysiwyg_imageupload/3998/2015/12/02/JPMobasserMD_2.jpg"> 
          <figcaption>Patient ID</figcaption>
        </figure>
        
      </slide>
      !-->
    </carousel-3d>
    <div id="output" style="display:none">
      <!--
      <v-btn id="btnNext" @click="nextSlide" color="success">Next</v-btn>
      <v-btn id="btnPrev" @click="prevSlide" color="success">Previous</v-btn>!-->
      <span data-id="btnNext" @click="nextSlide()"
        ><i class="fa fa-refresh"></i
      ></span>
    </div>
  </div>
</template>

<script type="text/javascript">
import dwv from "dwv";

export default {
  name: "Demo",
  data() {
    return {
      slides: [
        {
          name: "Slide name 1"
        },
        {
          name: "Slide name 2"
        },
        {
          name: "Slide name 3"
        },
        {
          name: "Slide name 4"
        },
        {
          name: "Slide name 5"
        }
      ]
    };
  },
  methods: {
    nextSlide() {
      this.$refs.mycarousel.goNext();
    },
    prevSlide() {
      this.$refs.mycarousel.goPrev();
    }
  },
  mounted() {
    var Leap = require("leapjs");
    var output = document.getElementById("output");
    const btnNext = document.querySelector('[data-id="btnNext"]');

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
      list0[i] = "Patient1/T1_TSE_TRA/D3/T1_TSE_TRA__0005_00" + (i+1) + ".dcm";
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
    for (var i = 0; i < 4; i++) {      
      if(i+6==10) {
        list1[i] = "Patient1/T1_TSE_TRA/D4/T1_TSE_TRA__0005_0" + (i+6) + ".dcm"; 
      } else {
        list1[i] = "Patient1/T1_TSE_TRA/D4/T1_TSE_TRA__0005_00" + (i+6) + ".dcm"; 
      }        
    }
    app1.loadURLs(list1);

    // create the third dwv app
    var app2 = new dwv.App();
    app2.init({
      containerDivId: "dwv2",
      fitToWindow: "true",
      tools: ["Scroll"]
    });
    var list2 = [];
    for (var i = 0; i < 4; i++) {
      list2[i] = "Patient1/T1_TSE_TRA/D5/T1_TSE_TRA__0005_0" + (i+11) + ".dcm";        
    }
    app2.loadURLs(list2);

    var app3 = new dwv.App();
    app3.init({
      containerDivId: "dwv3",
      fitToWindow: "true",
      tools: ["Scroll"]
    });
    var list3 = [];
    for (var i = 0; i < 15; i++) {
      if(i < 9) {
        list3[i] = "Patient1/T1_TSE_SAG/T1_TSE_SAG__0005_00" + (i+1) + ".dcm";
      } else {
        list3[i] = "Patient1/T1_TSE_SAG/T1_TSE_SAG__0005_0" + (i+1) + ".dcm";
      }            
    }
    app3.loadURLs(list3);

    var app4 = new dwv.App();
    app4.init({
      containerDivId: "dwv4",
      fitToWindow: "true",
      tools: ["Scroll"]
    });
    var list4 = [];
    for (var i = 0; i < 15; i++) {
      if(i < 9) {
        list4[i] = "Patient1/T2_TSE_SAG/T2_TSE_SAG__0001_00" + (i+1) + ".dcm";
      } else {
        list4[i] = "Patient1/T2_TSE_SAG/T2_TSE_SAG__0001_0" + (i+1) + ".dcm";
      }            
    }
    app4.loadURLs(list4);

    Leap.loop(function(frame) {
      output.innerHTML =
        "<div style='width:300px; float:left; padding:5px'>" +
        "Frame: " +
        frame.id +
        "</div>";

      if (frame.gestures.length > 0 && frame.id % 15 === 0) {
        btnNext.click();
      }
    });
  }
};
</script>

<style scoped>
.mainDiv {
  background-color: black;
  padding-top: 3%;
  padding-bottom: 12%;
}
.carousel-3d-container {
  padding-top: 0%;
}
.carousel-3d-slide {
  padding: 0px;
}
.carousel-3d-container figure {
  margin: 0;
}

.carousel-3d-container figcaption {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  color: #fff;
  bottom: 0;
  position: absolute;
  bottom: 0;
  padding: 15px;
  font-size: 12px;
  min-width: 100%;
  box-sizing: border-box;
}
</style>
