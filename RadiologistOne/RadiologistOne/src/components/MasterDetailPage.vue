<template>
  <div class="col">
    <div class="row heading">
      <div class="col">
        <h3 class="ml-3 mb-4">{{textSampleData.name}}</h3>
      </div>
    </div>
    <div class="row">
      <div class="col-12 mt-3">
        <b-breadcrumb class="bg-white">
          <b-breadcrumb-item href="#">Master Detail</b-breadcrumb-item>
          <b-breadcrumb-item active>{{textSampleData.name}}</b-breadcrumb-item>
        </b-breadcrumb>
      </div>
      <div class="col-md-8 col-12 ml-3 mb-5">
        <p class="title">Patient</p>
        <p>{{textSampleData.name}}</p>
        <p class="title">Order Date</p>
        <p>{{textSampleData.orderDate}}</p>
        <p class="title">Healthcare Provider</p>
        <p>{{textSampleData.shipFrom}}</p>
        <p class="title">Age</p>
        <p>{{textSampleData.age}}</p>
        <p class="title">Description</p>
        <p>{{textSampleData.shortDescription}}</p>
        <p class="title">Classification</p>
        <p>{{textSampleData.status}}</p>
        <p class="title">Probability</p>
        <p>{{textSampleData.probability}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MasterDetailPage",
  props: {
    textSampleData: {
      type: Object,
      required: true,
      validator: function(value) {
        return (
          value.id !== undefined &&
          value.longDescription !== undefined &&
          value.shortDescription !== undefined &&
          value.orderDate !== undefined &&
          value.age !== undefined &&
          value.shipFrom !== undefined &&
          value.status !== undefined &&
          value.probability !== undefined &&
          value.name !== undefined
        );
      }
    }
  }
};
</script>

<style scoped>
.title {
  font-weight: 700;
  margin-bottom: 0;
}

.breadCrumbLink {
  color: #025fce;
}

.heading {
  background-color: #cecece;
  padding-top: 18em;
}
</style>
