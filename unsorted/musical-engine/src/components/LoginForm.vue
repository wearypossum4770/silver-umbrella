<template>
  <div>
    <!-- https://mlsdev.com/amp/blog/how-to-build-an-ecommerce-website-from-scratch -->
    <form @submit.prevent method="post">
      <div class="imgcontainer" @click="getFile">
        <img
          src="@/assets/profile_images/default.webp"
          alt="Avatar"
          class="avatar"
          autocomplete="photo"
        />
      </div>
      <div class="container">
        <label for="username"><b>Username</b></label>
        <input
          type="text"
          v-model="username"
          autocomplete="username"
          value="genryusai.shigekuni.yamamoto"
          required
        />
        <label for="psw"><b>Password</b></label>
        <input
          :type="passwordFieldType"
          v-model="password"
          autocomplete="current-password"
          value="RzMdsJLufx2FvVi"
          required
        />
        <button type="button" @click="switchVisibility">SHOW</button>
        <button type="submit" @click="handleLogin">Login</button>
        <label>
          <input type="checkbox" v-model="rememberMe" name="remember" />
          Remember me
        </label>
      </div>
      <div class="container" style="background-color: #f1f1f1">
        <button type="button" class="cancelbtn">Cancel</button>
        <span class="psw">Forgot <a href="#">password?</a></span>
      </div>
    </form>
  </div>
</template>
<script>
export default {
  name: "LoginForm",
  methods: {
    async getFile() {
      [this.fileHandle] = await window.showOpenFilePicker(this.pickerOpts);
      if (this.fileHandle.kind === "file") {
        this.profileImageChanged = true;
        const fileData = await this.fileHandle.getFile();
        Object.assign(this.profileImage, fileData);
      }
    },
    gatherData() {
      this.fromData.set("password", this.password);
      this.fromData.set("username", this.username);
      if (this.profileImageChanged) {
        this.fromData.set("profileImage", this.profileImage);
      }
      return JSON.stringify(Object.fromEntries(this.fromData.entries()));
    },
    async switchVisibility() {
      this.passwordFieldType =
        this.passwordFieldType === "password" ? "text" : "password";
    },
    async uploadImage() {},
    async handleLogin() {
      try {
        this.gatherData();
        const resp = await (
          await fetch("http://localhost:3002/login/", {
            ...this.setOptions,
            body: this.gatherData(),
          })
        ).json();
        if (resp.isAuthenticated) {
          console.log(resp);
          // this.password = "";
          // this.username = "";
          return;
        }
        throw Error;
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    optionsMap() {
      return new Map();
    },
    setOptions() {
      return Object.fromEntries([
        ["mode", "cors"],
        ["method", "POST"],
        ["headers", new Headers([["Content-Type", "application/json"]])],
      ]);
    },
  },
  data() {
    return {
      pickerOpts: {
        types: [
          {
            description: "Images",
            accept: {
              "image/*": [".png", ".gif", ".jpeg", ".jpg"],
            },
          },
        ],
        excludeAcceptAllOption: true,
        multiple: false,
      },
      fromData: new Map(),
      profileImage: {},
      profileImageChanged: false,
      fileHandle: null,
      passwordFieldType: "password",
      rememberMe: false,
      password: "RzMdsJLufx2FvVi",
      username: "genryusai.shigekuni.yamamoto",
    };
  },
};
</script>
<style scoped>
.field-icon {
  float: right;
  margin-left: -25px;
  margin-top: -25px;
  position: relative;
  z-index: 2;
}
form {
  border: 3px solid #f1f1f1;
}
input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}
button {
  background-color: #04aa6d;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}
button:hover {
  opacity: 0.8;
}
.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}
.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}
img.avatar {
  width: 40%;
  border-radius: 50%;
}
.container {
  padding: 16px;
}
span.psw {
  float: right;
  padding-top: 16px;
}
@media screen and (max-width: 300px) {
  span.psw {
    display: block;
    float: none;
  }
  .cancelbtn {
    width: 100%;
  }
}
</style>
