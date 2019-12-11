<template>
  <div class="text-center header">
        <h1>About Our App</h1>
        <br>
        <div class="row">
            <div class="container">
              <p>
              Our app, is the best tool to help radiologist reducing routine, time-consuming tasks while it automatically review pending medical images, prioritizing only the highest-risk patient for further evaluation and reducing clinical workload.
              </p>
            </div>
        </div> 
        <div class="row">
            <div class="container">
              <p>
                Initially, our app takes a medical image to see if it automatically detect bulge, protrusion or herniation in the lumbar spinal cord assigning priority to those patients that are more likely to have a stenosis.
              </p>
            </div> 
          </div>
        </div>       
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
  padding-top: 4rem;
  padding-bottom: 12rem;
}
.center {
  text-align: center;
  padding-left: 10rem;
  padding-right: 10rem;
  padding-top: 1rem;
}

.container {
  padding-right: 70px;
  padding-left: 70px;
  margin-right: auto;
  margin-left: auto;
  font-size: 20px;
}



</style>
