<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld/>
    <HelloCard msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import HelloCard from "@/components/HelloCard.vue";

export default {
  name: "home",
  components: {
    HelloWorld,
    HelloCard
  }
};
</script>
