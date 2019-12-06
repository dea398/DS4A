<template>
  <div class="text-center header">
        <h1>About Our App</h1>
        <p>
        </p>
        <p class="center">
          Our app, is the best tool to help radiologist reducing routine, time-consuming tasks while it automatically review pending medical images, prioritizing only the highest-risk patient for further evaluation and reducing clinical workload.</p>
        <p class="center">
          Initially, our app takes a medical image to see if it automatically detect bulge, protrusion or herniation in the lumbar spinal cord assigning priority to those patients that are more likely to have a stenosis.
        </p>        
  </div>
</template>

<script>

export default {
  name: "Description"
};
</script>

<style scoped>
.header {
  background-color: #cecece;
  padding-top: 3rem;
  padding-bottom: 7rem;
}
.center {
  text-align: center;
  padding-left: 10rem;
  padding-right: 10rem;
  padding-top: 1rem;
}
</style>
