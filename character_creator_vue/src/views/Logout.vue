<template></template>

<script>
export default {
  created() {
    this.$store.dispatch("userLogout").then(() => {
      this.$router.push({ name: "CharacterCreation" });
    });
  },
};
</script>