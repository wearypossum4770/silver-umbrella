"use strict";

import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

const moduleA = {
  state: () => ({
    socket: {
      isConnected: false,
      connection: null,
      message: "",
      reconnectError: false,
    },
  }),
  mutations: {
    sendMessageJSON(state, payload) {
      state.socket.connection.send(JSON.stringify(payload.message));
    },
    sendMessage(state, payload) {
      state.socket.connection.send(payload.message);
    },
    onopen(state, payload) {
      Vue.prototype.$socket = payload.currentTarget;
      state.socket.isConnected = true;
      console.log("Successfully connected to the echo websocket server...");
    },
    onclose(state) {
      state.socket.connection.close(1000);
      state.socket.isConnected = false;
    },
    onmessage(state, payload) {
      return payload.message;
    },
    onerror(state, payload) {},
  },
  actions: {
    sendMessage(context) {
      context.commit("sendMessage");
      Vue.prototype.$socket.send(message);
    },
  },
  getters: {},
};
const state = {
  socket: {
    isConnected: false,
    message: "",
    reconnectError: false,
  },
};
let _websocket = new WebSocket("ws://localhost:7625");
_websocket.onopen = function (event) {
  Vue.prototype.$socket = event.currentTarget;
  state.socket.isConnected = true;
  console.log("Successfully connected to the echo websocket server...");
};
_websocket.onclose = function (event) {};
_websocket.onmessage = function (event) {
  return event.message;
};
_websocket.onerror = function (event) {};
Plugin.install = (Vue, options) => {
  Vue.websocket = _websocket;
  window.websocket = _websocket;
  Vue.mixin({
    created: function () {},
  });
  Vue.prototype.$onmessage = function () {
    _websocket.onmessage;
  };
};
Vue.use(Plugin);
export default Plugin;
