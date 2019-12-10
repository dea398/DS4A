<template>
  <div>
    <main id="mainContent">
      <div class="text-center header">
        <h1>We are the team #1 of the DS4A in Medellín - Colombia.</h1>
        <p></p>
      </div>

      <div class="container">
        <div class="row justify-content-center py-5">
          <h1>Team Members</h1>
        </div>

        <div class="row justify-content-around text-center pb-5">
          <div class="container">
            <div class="row blog">
              <div class="col-md-12">
                <div
                  id="blogCarousel"
                  class="carousel slide"
                  data-ride="carousel"
                >
                  <!-- Carousel items -->
                  <div class="carousel-inner">
                    <div class="carousel-item active">
                      <div class="row">
                        <div class="col-lg-3 col-md-6 col-sm-6">
                          <div class="our-team">
                            <div class="pic">
                              <img src="Edwin.jpg" />
                            </div>
                            <div class="team-content">
                              <h3 class="title">Edwin Duque</h3>
                              <span class="post"
                                >System Engineering, Msc HCI, PhD (s)</span
                              >
                            </div>
                            <ul class="social">
                              <li>
                                <a
                                  href="Edwin-D-Resume.pdf"
                                  class="fa fa-envelope"
                                  >Resume</a
                                >
                              </li>
                            </ul>
                          </div>
                        </div>

                        <div class="col-lg-3 col-md-6 col-sm-6">
                          <div class="our-team">
                            <div class="pic">
                              <img src="Ruben.jpeg" />
                            </div>
                            <div class="team-content">
                              <h3 class="title">Ruben Yepes</h3>
                              <span class="post"
                                >Statistician, MSC in Economics</span
                              >
                            </div>
                            <ul class="social">
                              <li>
                                <a
                                  href="Ruben-Y-Resume.pdf"
                                  class="fa fa-envelope"
                                  >Resume</a
                                >
                              </li>
                            </ul>
                          </div>
                        </div>
                        <div class="col-lg-3 col-md-6 col-sm-6">
                          <div class="our-team">
                            <div class="pic">
                              <img src="Florez.jpeg" />
                            </div>
                            <div class="team-content">
                              <h3 class="title">Sebastian Florez</h3>
                              <span class="post"
                                >System Engineering, GCert in Analytics</span
                              >
                            </div>
                            <ul class="social">
                              <li>
                                <a
                                  href="Sebas-Florez-Resume.pdf"
                                  class="fa fa-envelope"
                                  >Resume</a
                                >
                              </li>
                            </ul>
                          </div>
                        </div>

                        <div class="col-lg-3 col-md-6 col-sm-6">
                          <div class="our-team">
                            <div class="pic">
                              <img src="Zambrano.jpeg" />
                            </div>
                            <div class="team-content">
                              <h3 class="title">Sebastian Zambrano</h3>
                              <span class="post">Business Administrator</span>
                            </div>
                            <ul class="social">
                              <li>
                                <a
                                  href="Sebas-Zambrano-Resume.pdf"
                                  class="fa fa-envelope"
                                  >Resume</a
                                >
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                      <!--.row-->
                    </div>
                  </div>
                  <!--.carousel-inner-->
                </div>
                <!--.Carousel-->
              </div>
            </div>
          </div>
          <p>(Mouse over them to see resume)</p>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: "Who_We_Are"
};
</script>

<style scoped>
.header {
  background-color: #cecece;
  padding-top: 1rem;
  padding-bottom: 0rem;
}

h1 {
  margin-top: 0;
  font-size: 2rem;
  display: inline-block;
}
h1 div {
  position: relative;
  float: left;
}
h1 div:first-child {
  color: #3498db;
  margin-right: 1rem;
}
/* PROFIL */
.blog .carousel-indicators {
  left: 0;
  top: auto;
  bottom: -40px;
}

/* The colour of the indicators */
.blog .carousel-indicators li {
  background: #a3a3a3;
  border-radius: 50%;
  width: 8px;
  height: 8px;
  margin-bottom: 10px;
}

.blog .carousel-indicators .active {
  background: #707070;
  margin-bottom: 10px;
}

.our-team-section {
  position: relative;
  padding-top: 40px;
  padding-bottom: 40px;
}
.our-team-section:before {
  position: absolute;
  top: -0;
  left: 0;
  content: " ";
  background-size: 100% 100px;
  width: 100%;
  height: 100px;
  float: left;
  z-index: 99;
}
.our-team {
  padding: 0 0 40px;
  background: #f9f9f9;
  text-align: center;
  overflow: hidden;
  position: relative;
  border-bottom: 5px solid #00325a;
}
.our-team:hover {
  border-bottom: 5px solid #2f2f2f;
}

.our-team .pic {
  display: inline-block;
  width: 130px;
  height: 130px;
  margin-bottom: 50px;
  z-index: 1;
  position: relative;
}
.our-team .pic:before {
  content: "";
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: #00325a;
  position: absolute;
  bottom: 135%;
  right: 0;
  left: 0;
  opacity: 1;
  transform: scale(3);
  transition: all 0.3s linear 0s;
}
.our-team:hover .pic:before {
  height: 100%;
  background: #2f2f2f;
}
.our-team .pic:after {
  content: "";
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: #ffffff00;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
  transition: all 0.3s linear 0s;
}
.our-team:hover .pic:after {
  background: #7ab92d;
}
.our-team .pic img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  transform: scale(1);
  transition: all 0.9s ease 0s;
  box-shadow: 0 0 0 14px #f7f5ec;
  transform: scale(0.7);
  position: relative;
  z-index: 2;
}
.our-team:hover .pic img {
  box-shadow: 0 0 0 14px #f7f5ec;
  transform: scale(0.7);
}
.our-team .team-content {
  margin-bottom: 30px;
}
.our-team .title {
  font-size: 22px;
  font-weight: 700;
  color: #4e5052;
  letter-spacing: 1px;
  text-transform: capitalize;
  margin-bottom: 5px;
}
.our-team .post {
  display: block;
  font-size: 15px;
  color: #4e5052;
  text-transform: capitalize;
}
.our-team .social {
  width: 100%;
  padding-top: 10px;
  margin: 0;
  background: #2f2f2f;
  position: absolute;
  bottom: -100px;
  left: 0;
  transition: all 0.5s ease 0s;
}
.our-team:hover .social {
  bottom: 0;
}
.our-team .social li {
  display: inline-block;
}
.our-team .social li a {
  display: block;
  padding-top: 6px;
  font-size: 15px;
  color: #fff;
  transition: all 0.3s ease 0s;
}
.our-team .social li a:hover {
  color: #2f2f2f;
  background: #f7f5ec;
}
@media only screen and (max-width: 990px) {
  .our-team {
    margin-bottom: 10px;
  }
}
</style>
