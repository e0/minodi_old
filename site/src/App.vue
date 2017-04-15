<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'app'
}

</script>

<style lang="scss">

body {
  background-color: #fefefe;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  max-width: 1200px;
  margin: 42px auto 0 auto;

  p {
    font-size: 21px;
  }

  h1 {
    font-size: 42px;
  }

  h2 {
    font-size: 28px;
  }

  .subtitle {
    margin-top: -21px;
    margin-bottom: 42px;
    font-style: italic;
  }
}

@media all and (max-width: 1024px) {
  #app {
    max-width: 100%;
    margin: 21px;

    h2 {
      font-size: 21px;
    }
  }
}
</style>
