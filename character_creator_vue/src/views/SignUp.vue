<template>
  <div>
    <form v-on:submit.prevent="signup">
      <p v-if="!match">Your Password doesn't match please try again.</p>
      <div>
        <label for="username">username</label>
        <input v-model="username" id="username" type="text" />
      </div>
      <div>
        <label for="password">Password</label>
        <input v-model="password1" id="password1" type="password" />
      </div>
      <div>
        <label for="password">Re-enter Password</label>
        <input v-model="password2" id="password2" type="password" />
      </div>
      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SignUp",

  data() {
    return {
      username: "",
      password1: "",
      password2: "",
      match: true,
    };
  },
  methods: {
    matched() {
      if (this.password1 === this.password2) {
        return true;
      } else {
        match = false;
        return false;
      }
    },
    signup() {
      if (this.matched()) {
        axios({
          method: "post",
          url: "http://127.0.0.1:5050/create/",
          data: {
            username: this.username,
            password: this.password1,
          },
        }).then(() => this.$router.push({ name: "login" }));
      }
    },
  },
};
</script>