<template>
  <!-- https://bootsnipp.com/snippets/nNg98 -->
  <div>
    <div class="card-body contacts_body">
      <ul class="contacts">
        <li v-for="user in users" :key="user.id" class="w3-bar">
          <span
            onclick="this.parentElement.style.display='none'"
            class="w3-bar-item w3-button w3-xlarge w3-right"
            >&times;</span
          >
          <img
          @click="showAttr"
          :src="user.avatar"
            class="w3-bar-item w3-circle"
            style="width: 85px"
          />
          <div class="w3-bar-item">
            <span class="w3-large">{{ user.displayName }}</span
            ><br />
            <span>{{ user.lastUpdated }}</span>
          </div>
        </li>
      </ul>
    </div>

    <div>
      <ul id="messages">
        <li v-for="(value, name) in messages" :key="name">
          {{ value }}
        </li>
      </ul>
      <form id="form" @submit.prevent>
        <input :value="message" @input="updateMessage" autocomplete="off" />
        <button @click="sendMessage">Send</button>
      </form>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);
const store = new Vuex.Store({
  state: {
    websocket: null,
    reconnectError: false,
    websocketClosed: true,
    websocketConnected: false,
    message: "",
    debug: { errors: null, _console: "" },
    websocketError: null,
    messageArr: [],
  },
  mutations: {
    sendMessage({ websocket, message, messageArr }) {
      messageArr.push(message);
      websocket.send(JSON.stringify({ message: message }));
    },
    clearMessage(state) {
      state.message = "";
    },
    updateMessage(state, message) {
      state.message = message;
    },
    createConnection(state) {
      state.websocket = new WebSocket(
        "ws://localhost:7625/ws/chat/private/group/channel/genryusai.shigekuni.yamamoto/greetings/bitch",
      );
      state.websocket.onopen = function () {
        state.websocketClosed = false;
        state.websocketConnected = true;
      };
      state.websocket.heartbeat = function (event) {
        state.websocket.send("heartbeat");
        console.log(event);
      };
      state.websocket.onerror = function (event) {
        state.debug["errors"] = [...state.debug["errors"], event.message];
        state.websocketError = event.message;
      };
      state.websocket.onclose = function () {
        state.websocketClosed = true;
        state.websocketConnected = false;
      };
      (state.websocket.onheartbeat = function (event) {
        console.log(event);
      }),
        (state.websocket.onmessage = function ({ data }) {
          let _message = JSON.parse(data);
          if (_message.message === "connected") {
            state.debug["_console"] = [
              ...state.debug["_console"],
              "Successfully connected to the echo websocket server...",
            ];
          } else {
            state.messageArr.push(_message.message);
          }
        });
    },
  },
});
export default {
  name: "Chat",
  data() {
    return {
      store,
      users: [
        {
          id: 1,
          isOnline: true,
          username: "",
          displayName: "Khalid",
          lastUpdated: "",
          avatar: '@/assets/profile_images/default.webp',
        },
        {
          id: 2,
          isOnline: false,
          username: "sui.feng",
          displayName: "Suì-Fēng",
          lastUpdated: "7 mins ago",
          avatar: '@/assets/profile_images/sui.feng.png',
        },
        {
          id: 3,
          isOnline: true,
          username: "byakuya.kuchiki",
          displayName: "Byakuya Kuchiki",
          lastUpdated: "",
          avatar: '@/assets/profile_images/byakuya.kuchiki.png',
        },
        {
          id: 4,
          isOnline: false,
          username: "shunsui.kyoraku",
          displayName: "Shunsui Kyōraku",
          lastUpdated: "30 mins ago",
          avatar: '@/assets/profile_images/shunsui.kyoraku.png',
        },
        {
          id: 5,
          isOnline: false,
          avatar: '@/assets/profile_images/toshiro.hitsugaya.png',
          username: "toshiro.hitsugaya",
          displayName: "Tōshirō Hitsugaya",
          lastUpdated: "left 50 mins ago",
        },
        {
          id: 6,
          isOnline: true,
          avatar: '@/assets/profile_images/genryusai.shigekuni.yamamoto.png',
          username: "genryusai.shigekuni.yamamoto",
          displayName: "Captain Yamamoto",
          lastUpdated: "",
        },
      ],
      message: "",
      username: "genryusai.shigekuni.yamamoto",
      password: "RzMdsJLufx2FvVi",
    };
  },
  mounted: function () {
    this.$nextTick(function () {
      store.commit("createConnection");
    });
  },
  computed: {
    messages: function () {
      return store.state.messageArr.reduce((total, current, index) => {
        total[index] = current;
        return total;
      }, {});
    },
  },
  methods: {
    showAttr(event){
      console.log(event)
      console.log(event.target.src)
    },
        getAvatar(user){
          return require(user.avatar)
        },

    sendMessage() {
      store.commit("sendMessage");
      this.message = "";
    },
    updateMessage(e) {
      let { value } = e.target;
      this.message = value;
      store.commit("updateMessage", value);
    },
  },
};
</script>

<style scoped>
body,
html {
  height: 100%;
  margin: 0;
  background: #7f7fd5;
  background: -webkit-linear-gradient(to right, #91eae4, #86a8e7, #7f7fd5);
  background: linear-gradient(to right, #91eae4, #86a8e7, #7f7fd5);
}

.chat {
  margin-top: auto;
  margin-bottom: auto;
}
.card {
  height: 500px;
  border-radius: 15px !important;
  background-color: rgba(0, 0, 0, 0.4) !important;
}
.contacts_body {
  padding: 0.75rem 0 !important;
  overflow-y: auto;
  white-space: nowrap;
}
.msg_card_body {
  overflow-y: auto;
}
.card-header {
  border-radius: 15px 15px 0 0 !important;
  border-bottom: 0 !important;
}
.card-footer {
  border-radius: 0 0 15px 15px !important;
  border-top: 0 !important;
}
.container {
  align-content: center;
}
.search {
  border-radius: 15px 0 0 15px !important;
  background-color: rgba(0, 0, 0, 0.3) !important;
  border: 0 !important;
  color: white !important;
}
.search:focus {
  box-shadow: none !important;
  outline: 0px !important;
}
.type_msg {
  background-color: rgba(0, 0, 0, 0.3) !important;
  border: 0 !important;
  color: white !important;
  height: 60px !important;
  overflow-y: auto;
}
.type_msg:focus {
  box-shadow: none !important;
  outline: 0px !important;
}
.attach_btn {
  border-radius: 15px 0 0 15px !important;
  background-color: rgba(0, 0, 0, 0.3) !important;
  border: 0 !important;
  color: white !important;
  cursor: pointer;
}
.send_btn {
  border-radius: 0 15px 15px 0 !important;
  background-color: rgba(0, 0, 0, 0.3) !important;
  border: 0 !important;
  color: white !important;
  cursor: pointer;
}
.search_btn {
  border-radius: 0 15px 15px 0 !important;
  background-color: rgba(0, 0, 0, 0.3) !important;
  border: 0 !important;
  color: white !important;
  cursor: pointer;
}
.contacts {
  list-style: none;
  padding: 0;
}
.contacts li {
  width: 100% !important;
  padding: 5px 10px;
  margin-bottom: 15px !important;
}
.active {
  background-color: rgba(0, 0, 0, 0.3);
}
.user_img {
  height: 70px;
  width: 70px;
  border: 1.5px solid #f5f6fa;
}
.user_img_msg {
  height: 40px;
  width: 40px;
  border: 1.5px solid #f5f6fa;
}
.img_cont {
  position: relative;
  height: 70px;
  width: 70px;
}
.img_cont_msg {
  height: 40px;
  width: 40px;
}
.online_icon {
  position: absolute;
  height: 15px;
  width: 15px;
  background-color: #4cd137;
  border-radius: 50%;
  bottom: 0.2em;
  right: 0.4em;
  border: 1.5px solid white;
}
.offline {
  background-color: #c23616 !important;
}
.user_info {
  margin-top: auto;
  margin-bottom: auto;
  margin-left: 15px;
}
.user_info span {
  font-size: 20px;
  color: white;
}
.user_info p {
  font-size: 10px;
  color: rgba(255, 255, 255, 0.6);
}
.video_cam {
  margin-left: 50px;
  margin-top: 5px;
}
.video_cam span {
  color: white;
  font-size: 20px;
  cursor: pointer;
  margin-right: 20px;
}
.msg_cotainer {
  margin-top: auto;
  margin-bottom: auto;
  margin-left: 10px;
  border-radius: 25px;
  background-color: #82ccdd;
  padding: 10px;
  position: relative;
}
.msg_cotainer_send {
  margin-top: auto;
  margin-bottom: auto;
  margin-right: 10px;
  border-radius: 25px;
  background-color: #78e08f;
  padding: 10px;
  position: relative;
}
.msg_time {
  position: absolute;
  left: 0;
  bottom: -15px;
  color: rgba(255, 255, 255, 0.5);
  font-size: 10px;
}
.msg_time_send {
  position: absolute;
  right: 0;
  bottom: -15px;
  color: rgba(255, 255, 255, 0.5);
  font-size: 10px;
}
.msg_head {
  position: relative;
}
#action_menu_btn {
  position: absolute;
  right: 10px;
  top: 10px;
  color: white;
  cursor: pointer;
  font-size: 20px;
}
.action_menu {
  z-index: 1;
  position: absolute;
  padding: 15px 0;
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border-radius: 15px;
  top: 30px;
  right: 15px;
  display: none;
}
.action_menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.action_menu ul li {
  width: 100%;
  padding: 10px 15px;
  margin-bottom: 5px;
}
.action_menu ul li i {
  padding-right: 10px;
}
.action_menu ul li:hover {
  cursor: pointer;
  background-color: rgba(0, 0, 0, 0.2);
}
@media (max-width: 576px) {
  .contacts_card {
    margin-bottom: 15px !important;
  }
}
</style>
