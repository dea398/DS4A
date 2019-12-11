<template>
  <div>
  <v-carousel>
    <v-carousel-item
      v-for="(item,i) in items"
        :key="i"
        :src="item.src"
        reverse-transition="fade-transition"
        transition="fade-transition"
    ></v-carousel-item>
  </v-carousel>  
  </div> 
</template>

<script>
export default {
  name: "EDA",  
  data () {
        return {
      items: [
        {
          src: 'Slides/slide1.PNG',          
        },
        {
          src: 'Slides/slide2.PNG', 
        },
        {
          src: 'Slides/slide3.PNG', 
        },
        {
          src: 'Slides/slide4.PNG', 
        },
        {
          src: 'Slides/slide5.PNG', 
        },
        {
          src: 'Slides/slide6.PNG', 
        },
        {
          src: 'Slides/slide7.PNG', 
        },
        {
          src: 'Slides/slide8.PNG', 
        },
        {
          src: 'Slides/slide9.PNG', 
        },
      ],
    }
  },
};
</script>

<style scoped></style>
