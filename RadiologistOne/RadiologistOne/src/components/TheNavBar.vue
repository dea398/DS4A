//TODO Web Template Studio: Add a new link in the NavBar for your page here.
// A skip link is included as an accesibility best practice. For more information visit https://www.w3.org/WAI/WCAG21/Techniques/general/G1.
<template>
  <div>
    <div class="skipLink">
      <a href="#mainContent">Skip to Main Content</a>
    </div>
    <b-nav class="navbar navbar-expand-sm navbar-light border-bottom justify-content-between">
      <a class="navbar-brand" href="/">Radiologist One</a>
      <div class="navbar-nav">
        <b-nav-item class="nav-item nav-link active" to="/Description">Description</b-nav-item>
        <b-nav-item class="nav-item nav-link active" to="/Who_We_Are">Who We Are</b-nav-item>
        <b-nav-item class="nav-item nav-link active" to="/EDA">Exploratory Data Analysis</b-nav-item>
        <b-nav-item class="nav-item nav-link active" to="/Demo">Demo</b-nav-item>
        <b-nav-item class="nav-item nav-link active" to="/Demo2">Demo 2</b-nav-item>
        <b-nav-item class="nav-item nav-link active" to="/Contact_Us">Contact Us</b-nav-item>
      </div>
    </b-nav>
  </div>
</template>

<script>
export default {
  name: "TheNavBar"
};
</script>

<style scoped>
.skipLink a {
  position: absolute;
  left: -100px;
  top: -100px;
}

.skipLink a:focus {
  position: fixed;
  z-index: 1000;
  top: 0;
  left: 0;
  padding: 10px;
  color: #ffffff;
  background: #000000;
}
</style>
