<template>
  <div>
    <p v-if="incorrectAuth">
      Incorrect username or password entered - please try again
    </p>
    <form v-on:submit.prevent="login">
      <div class="form-group">
        <input
          type="text"
          name="username"
          id="user"
          v-model="username"
          class="form-control"
          placeholder="Username"
        />
      </div>
      <div class="form-group">
        <input
          type="password"
          name="password"
          id="pass"
          v-model="password"
          class="form-control"
          placeholder="Password"
        />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
      incorrectAuth: false,
    };
  },
  methods: {
    login() {
      this.$store
        .dispatch("userLogin", {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          this.$router.push({ name: "CharacterCreation" });
        })
        .catch((err) => {
          console.log(err);
          this.incorrectAuth = true;
        });
    },
  },
};
</script>