<template>
  <main id="mainContent">
    <div class="mainDiv">
      <carousel-3d :controls-visible="true" :clickable="true" 
      :perspective="40" :space="300" :width="450" :height="300">
        <slide v-for="(slide, i) in slides" :key=i :index="i">
          <figure>
            <img src="https://www.spineuniverse.com/sites/default/files/imagecache/gallery-large/wysiwyg_imageupload/3998/2015/12/02/JPMobasserMD_2.jpg">
            <figcaption>
              The sky is the limit only for those who aren't afraid to fly!
                        The sky is the limit only for those who aren't afraid to fly!

            </figcaption>
          </figure>
        </slide>
      </carousel-3d>   
    <div id="output"></div>

    </div>
  </main>
  
</template>

<script type="text/javascript">
    export default 
    {
      name: "Demo",
      data () 
      {
          return {
            slides:
            [
              {
                name: 'Slide name 1'
              }, 
              {
                name: 'Slide name 2'
              }, 
              {
                name: 'Slide name 3'
              }, 
              {
                name: 'Slide name 4'
              }, 
              {
                name: 'Slide name 5'
              }, 
              {
                name: 'Slide name 6'
              }, 
              {
                name: 'Slide name 7'
              }
            ]
          }
        }, 
       mounted() {
        var Leap = require('leapjs')  
        var output = document.getElementById('output');
        Leap.loop(function (frame) {
        output.innerHTML = "<div style='width:300px; float:left; padding:5px'>" + "Frame: " + frame.id + "</div>";
  });
       }
    
    }; 
    
</script>

<style scoped>
  .mainDiv
  {
    background-color: black;
    padding-top: 5%;
    padding-bottom:10%;
  }
  .carousel-3d-container{
      padding-top: 1%;
  }
  .carousel-3d-slide {
    padding: 0px;
  }
  .carousel-3d-container figure {
  margin:0;
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
