<template>
  <div>
    <main id="mainContent" class="container-fluid">
      <div class="row">
        <div class="col-2 p-0 border-right sidebar">
          <v-btn
            id="btnRank"
            class="ma-2"
            @click="fetchTextAssets2()"
            color="info"
            :loading="loading2"
            :disabled="loading2"
          >
            Rank Patients
            <template v-slot:loader>
              <span>Ranking...</span>
            </template>
          </v-btn>
          <div class="list-group list-group-flush border-bottom">
            <transition-group name="items" tag="div">
              <MasterDetailSideBarTab
                v-for="(textAssets, index) in masterDetailText"
                :key="textAssets.id"
                :index="index"
                :tabText="textAssets.name"
                :textSampleData="masterDetailText[index]"
                @onDisplayTabClick="handleDisplayTabClick"
              />
            </transition-group>
          </div>
        </div>
        <MasterDetailPage
          style="height: 600px;"
          :textSampleData="masterDetailText[currentDisplayTabIndex]"
        />
      </div>
    </main>
    <BaseWarningMessage
      v-if="WarningMessageOpen"
      :text="WarningMessageText"
      @onWarningClose="handleWarningClose"
    />
  </div>
</template>

<script>
import CONSTANTS from "@/constants";
import MasterDetailPage from "@/components/MasterDetailPage";
import MasterDetailSideBarTab from "@/components/MasterDetailSideBarTab";
import BaseWarningMessage from "@/components/BaseWarningMessage";

export default {
  name: "Demo2",

  components: {
    MasterDetailPage,
    MasterDetailSideBarTab,
    BaseWarningMessage
  },

  data() {
    return {
      loader: null,
      loading2: false,
      masterDetailText: [
        {
          id: 0,
          longDescription: "",
          shortDescription: "",
          orderDate: "",
          age: 0,
          shipFrom: "",
          status: "",
          probability: 0,
          name: ""
        }
      ],
      currentDisplayTabIndex: 0,
      WarningMessageOpen: false,
      WarningMessageText: ""
    };
  },

  created() {
    this.fetchTextAssets();
    // this.fetchTextAssets2();
  },
  watch: {
    loader() {
      const l = this.loader;
      this[l] = !this[l];

      setTimeout(() => (this[l] = false), 4000);
      //this.masterDetailText = this._.shuffle(this.masterDetailText);
      this.masterDetailText = this._.orderBy(
        this.masterDetailText,
        "probability",
        "desc"
      );
      this.loader = null;
    }
  },
  methods: {
    fetchTextAssets() {
      fetch(CONSTANTS.ENDPOINT.MASTERDETAIL)
        .then(response => {
          if (!response.ok) {
            throw Error(response.statusText);
          }
          return response.json();
        })
        .then(result => {
          this.masterDetailText = result;
        })
        .catch(error => {
          this.WarningMessageOpen = true;
          this.WarningMessageText = `${CONSTANTS.ERROR_MESSAGE.MASTERDETAIL_GET} ${error}`;
        });
    },
    fetchTextAssets2() {
      fetch(CONSTANTS.ENDPOINT.MASTERDETAIL2)
        .then(response => {
          if (!response.ok) {
            throw Error(response.statusText);
          }
          return response.json();
        })
        .then(result => {
          this.masterDetailText = result;
          this.loader = "loading2";
        })
        .catch(error => {
          this.WarningMessageOpen = true;
          this.WarningMessageText = `${CONSTANTS.ERROR_MESSAGE.MASTERDETAIL_GET} ${error}`;
        });
    },
    handleWarningClose() {
      this.WarningMessageOpen = false;
      this.WarningMessageText = "";
    },
    handleDisplayTabClick(id) {
      this.currentDisplayTabIndex = id;
    }
  }
};
</script>

<style scoped>
.custom-loader {
  animation: loader 1s infinite;
  display: flex;
}

.sidebar {
  /* full height - footer height - navbar height */
  min-height: calc(100vh - 160px - 57px);
}
#app .items-move {
  transition: transform 4s;
}
</style>
