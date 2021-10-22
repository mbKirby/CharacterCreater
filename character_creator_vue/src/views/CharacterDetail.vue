<template>
  <div>
    {{ character }}
  </div>
</template>
<script>
import axios from "axios";
export default {
  props: ["characterName"],
  data() {
    return {
      character: {},
    };
  },
  methods: {
    getCharacter() {
      axios({
        method: "get",
        url: "http://127.0.0.1:5050/characters/" + `${this.characterName}`,
        headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
      })
        .then((response) => {
          this.character = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mounted() {
    this.getCharacter();
  },
};
</script>