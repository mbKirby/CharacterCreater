<template>
  <div>
    <p>you made it</p>
    <div :key="character" v-for="character in data">
      {{ character.name }}
    </div>
  </div>
</template>

<script>
export default {
  computed: mapState(["data"]),
};
</script>