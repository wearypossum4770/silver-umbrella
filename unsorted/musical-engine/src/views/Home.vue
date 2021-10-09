<template>
  <div class="home">
    <div class="w3-row">
      <div class="w3-col m4 l3">
        <div v-for="user in users" :key="user.id">
          {{ user.name }}
          <button class="w3-btn w3-blue" @click="registerUser(user)">
            Register
          </button>
        </div>
      </div>
      <div class="w3-col m8 l9">
        <h3>Registered</h3>
        <h5>Total: {{ total }}</h5>
        <div v-for="registration in registrations" :key="registration.id">
          <div>{{ registration.name }}</div>
          <span class="w3-btn w3-red" @click="unregister(registration)"
            >UnRegister</span
          >
          <div class="date">{{ registration.date }}</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Home",
  methods: {
    unregister(registration) {
      let { users, registrations } = this.$store.state;
      const user = users.find(user => user.id == registration.id);
      user.registered = false;
      registrations.splice(registrations.indexOf(registration), 1);
    },
    registerUser(user) {
      let { registrations } = this.$store.state;
      const date = new Date();
      user.registered = true;
      return registrations.push({
        id: user.id,
        name: user.name,
        date: `${date.getMonth()}/${date.getDay()}`,
      });
    },
  },
  computed: {
    registrations() {
      return this.$store.state.registrations;
    },
    total() {
      return this.$store.state.registrations.length;
    },
    users() {
      return this.$store.state.users.filter(user => !user.registered);
    },
  },
};
</script>
