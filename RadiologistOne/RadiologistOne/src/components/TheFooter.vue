<template>
  <footer class="footer">
    <div class="container-fluid">
      <div class="row justify-content-around">
        <div class="col-8 col-md-5">
          <h5 class="title">Radiologist One</h5>
          <p class="description">This is an app created by Team 1 from Medellín. Data Science For All training in charged of MinTic and CorrelationOne.</p>
        </div>
        <div class="col-2">
          <ul class="list-unstyled">
            <li>
              <a class="footerlink" href="https://www.mintic.gov.co/">MinTic</a>
            </li>
            <li>
              <a class="footerlink" href="https://www.correlation-one.com/">CorrelationOne</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "TheFooter"
};
</script>


<style scoped>
.footer {
  background-color: white;
  padding-top: 2rem;
  padding-bottom: 4rem;
}

.title {
  color: black;
}

.description {
  color: black;
}

.footerlink,
.footerlink:hover {
  color: black;
}
</style>
