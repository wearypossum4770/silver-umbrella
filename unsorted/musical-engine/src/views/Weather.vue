<template>
  <div>
    <h1>{{ latitude }}</h1>
    <button @click="geoFindMe" class="w3-btn"><span>🌎</span> Locate Me</button>
    <button @click="fetchWeather">logit</button>
  </div>
</template>
<script>
export default {
  name: "Weather",
  data() {
    return {
      info: null,
    };
  },
  mounted() {
    this.axios
      .get("https://api.coindesk.com/v1/bpi/currentprice.json")
      .then(response => (this.info = response.data));
  },
  computed: {
    weather() {
      return this.$store.state.weather;
    },
    latitude() {
      return this.$store.state.latitude;
    },
    longitude() {
      return this.$store.state.longitude;
    },
  },
  methods: {
    async fetchWeather() {
      let { longitude, latitude, api_key } = await this.$store.state;
      if (longitude) {
        let url = `https://api.openweathermap.org/data/2.5/onecall?lat=${longitude}&lon=${latitude}&units=imperial&appid=${api_key}`;
        let response = await this.axios.get(url);
        this.$store.state.weather = response.data;
      } else {
        alert("Please press locate me");
      }
    },
    async geoFindMe() {
      if (this.$store.state.geoLocationSupported) {
        await navigator.geolocation.getCurrentPosition(position => {
          let { latitude, longitude } = position.coords;
          this.$store.state.latitude = latitude;
          this.$store.state.longitude = longitude;
        });
      }
    },
  },
};
</script>

<style scoped>
button {
  text-align: "center";
  font-size: "25px";
}
</style>
