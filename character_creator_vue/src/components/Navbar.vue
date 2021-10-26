<template>
  <div>
    <div>
      <img
        style="height: auto width:100%"
        class="img-fluid"
        src="CharacterCreator\character_creator_vue\src\assets\navbarpic3.jpgCharacterCreator\character_creator_vue\src\assets\navbarpic3.jpg"
        alt="party inside tavern"
      />
    </div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div>
        <div class="container-fluid">
          <a class="navbar-brand" href="#"></a>
          <!-- <h3 v-if="this.$store.getters.loggedIn">
        Hello, {{ username[0].username }}
      </h3> -->

          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="/">Home</a>
              </li>
              <li v-if="!this.$store.getters.loggedIn" class="nav-item">
                <a class="nav-link active" aria-current="page" href="Login"
                  >Login</a
                >
              </li>

              <li v-if="!this.$store.getters.loggedIn" class="nav-item">
                <a class="nav-link active" aria-current="page" href="sign-up"
                  >Sign Up</a
                >
              </li>
              <li v-if="this.$store.getters.loggedIn">
                <a
                  class="nav-link active"
                  aria-current="page"
                  href="character-sheet"
                  >Characters</a
                >
              </li>

              <li v-if="this.$store.getters.loggedIn">
                <a class="nav-link active" aria-current="page" href="Logout"
                  >Log out</a
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";
export default {
  name: "Navbar",
  computed: mapState(["data", "username"]),
  methods: {
    // getUser() {
    //   axios({
    //     method: "get",
    //     url: "http://127.0.0.1:5050/user/",
    //     headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
    //   })
    //     .then((response) => {
    //       this.$store.state.username = response.data;
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
    // },
  },
  created() {
    // this.getUser();
  },
};
</script>