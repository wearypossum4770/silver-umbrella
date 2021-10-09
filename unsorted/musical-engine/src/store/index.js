import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);
// https://github.com/nathanboktae/robust-websocket
// https://github.com/uNetworking/uWebSockets.js/blob/master/examples/WebSockets.js
// https://github.com/websockets/ws#simple-server
export default new Vuex.Store({
  strict: true,
  getters: {},
  state: {
    count: 0,
    latitude: null,
    longitude: null,
    appConfig: {},
    weather: null,
    api_key: "7af4edd80277ecd98c9eb7b15f9cfb84",
    geoLocationSupported: "geolocation" in navigator,
    registrations: [],
    users: [
      { id: 1, name: "Max", registered: false },
      { id: 2, name: "Anna", registered: false },
      { id: 3, name: "Chris", registered: false },
      { id: 4, name: "Sven", registered: false },
    ],
  },
  mutations: {},
  actions: {},
  modules: {},
});
