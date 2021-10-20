<template>
  <div>
    <p>hello</p>
    <form>
      <input type="text" name="username" id="username" />
      <input type="text" name="password1" id="password1" />
      <input type="text" name="password2" id="password2" />
      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "SignUp",

  data() {
    return {
      username: "",
      password1: "",
      password2: "",
    };
  },
  methods: {
    signup() {},
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