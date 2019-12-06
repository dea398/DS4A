<template>
  <div>
    <iframe frameborder="0" style="width: 100%; height: 350px; border:0" v-bind:src="'Datathon.html'"></iframe>
    <v-btn color="success">Success</v-btn>
    <jupyter-widget-embed
          voila-url="http://52.165.184.170"
          notebook="notebook2.ipynb"
          mount-id="test">
    </jupyter-widget-embed>
  </div>
  
</template>

<script >
export default {
  name: "EDA"
};
</script>

<style scoped>
</style>