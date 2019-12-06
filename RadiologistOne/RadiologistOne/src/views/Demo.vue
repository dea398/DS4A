<template>
  <div class="mainDiv">
    <carousel-3d
      ref="mycarousel"
      :controls-visible="true"
      :clickable="true"
      :perspective="0"
      :inverse-scaling="1500"
      :space="800"
      :width="650"
      :height="400"
    >
      <slide :index="0">
        <template>
          <div>
            <dwvVue style="width: 100%; height:500px;" />
          </div>
        </template>
      </slide>
      <slide :index="1">
        <template>
          <div>
            <dwvVue style="width: 100%; height:600px;" />
          </div>
        </template>
      </slide>
      <slide :index="2">
        <template>
          <div>
            <dwvVue style="width: 100%; height:700px;" />
          </div>
        </template>
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
    <div id="output">
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
import dwvVue from "@/components/dwv.vue";

export default {
  name: "Demo",
  components: {
    dwvVue
  },
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

    Leap.loop(function(frame) {
      output.innerHTML =
        "<div style='width:300px; float:left; padding:5px'>" +
        "Frame: " +
        frame.id +
        "</div>";

      if (frame.gestures.length > 0 && frame.id % 20 === 0) {
        btnNext.click();
      }
    });
  }
};
</script>

<style scoped>
.mainDiv {
  background-color: black;
  padding-top: 5%;
  padding-bottom: 10%;
}
.carousel-3d-container {
  padding-top: 1%;
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
