<template>
  <div>
    <form
      v-on:keyup="enterPressed"
      @submit.prevent
      style="border: 1px solid #ccc"
    >
      <div class="container">
        <h1>Sign Up</h1>
        <p>Please fill in this form to create an account.</p>
        <hr />
        <label html="firstName"><b> First Name</b></label>
        <input
          type="text"
          autocomplete="given-name"
          placeholder="Genryūsai"
          v-model="firstName"
        />
        <label html="middleName"><b>Middle Name</b></label>
        <input
          type="text"
          autocomplete="additional-name"
          placeholder="Shigekuni"
          v-model="middleName"
        />
        <label html="lastName"><b>Last Name</b></label>
        <input
          type="text"
          autocomplete="family-name"
          placeholder="Yamamoto"
          v-model="lastName"
        />
        <label html="username"><b>Username</b></label>
        <input
          type="text"
          autocomplete="username"
          placeholder="genryusai.shigekuni.yamamoto"
          v-model="username"
        />
        <label for="email"><b>Email</b></label>
        <input
          type="email"
          v-model="email"
          autocomplete="email"
          placeholder="genryusai.shigekuni.yamamoto@soul.society.com"
          name="email"
        />
        <label for="psw"><b>Password</b></label>
        <input
          type="password"
          v-model="password"
          autocomplete="new-password"
          placeholder="RzMdsJLufx2FvVi"
          name="psw"
        />
        <label for="psw-repeat"><b>Repeat Password</b></label>
        <input
          v-model="passwordConfirm"
          type="password"
          autocomplete="new-password"
          placeholder="RzMdsJLufx2FvVi"
          name="psw-repeat"
        />
        <label>
          <input
            type="checkbox"
            checked="checked"
            v-model="remeberMe"
            name="remember"
            style="margin-bottom: 15px"
          />
          Remember me
        </label>
        <p>
          By creating an account you agree to our
          <a href="#" style="color: dodgerblue">Terms & Privacy</a>.
        </p>
        <div class="clearfix">
          <button type="button" class="cancelbtn">Cancel</button>
          <button type="submit" v-on:click="registerUser" class="signupbtn">
            Sign Up
          </button>
        </div>
      </div>
    </form>
  </div>
</template>
<script>
export default {
  name: "Registration",
  data() {
    return {
      remeberMe: false,
      firstName: "Genryūsai",
      middleName: "Shigekuni",
      lastName: "Yamamoto",
      username: "genryusai.shigekuni.yamamoto",
      email: "genryusai.shigekuni.yamamoto@soul.society.com",
      password: "RzMdsJLufx2FvVi",
      passwordConfirm: "jfkRzMdsJLufx2FvVi",
    };
  },
  computed: {
    passwordssMatch() {
      return this.password === this.passwordConfirm;
    },
    setOptions() {
      return {
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
        method: "POST",
      };
    },
  },
  methods: {
    gatherData() {
      return JSON.stringify({
        email: this.email,
        password: this.password,
        remeberMe: this.remeberMe,
        firstName: this.firstName,
        middleName: this.middleName,
        lastName: this.lastName,
        username: this.username,
      });
    },
    enterPressed({ key, keyCode }) {
      if (key === "Enter" || keyCode === 13) {
        this.registerUser();
      }
    },
    // consider using axios instance for the vuex to pass url instead of entire url.
    async registerUser() {
      try {
        if (this.passwordssMatch) {
          const resp = await (
            await fetch("http://localhost:3002/bulk-create/", {
              ...this.setOptions,
              body: JSON.stringify({ user_list: this.user_list }),
            })
          ).json();
          this.firstName = "";
          this.middleName = "";
          this.lastName = "";
          this.username = "";
          this.email = "";
          this.password = "";
          this.passwordConfirm = "";
        }
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}
input[type="text"],
input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}
input[type="text"]:focus,
input[type="password"]:focus {
  background-color: #ddd;
  outline: none;
}
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}
button {
  background-color: #04aa6d;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}
button:hover {
  opacity: 1;
}
.cancelbtn {
  padding: 14px 20px;
  background-color: #f44336;
}
.cancelbtn,
.signupbtn {
  float: left;
  width: 50%;
}
.container {
  padding: 16px;
}
.clearfix::after {
  content: "";
  clear: both;
  display: table;
}
@media screen and (max-width: 300px) {
  .cancelbtn,
  .signupbtn {
    width: 100%;
  }
}
</style>
