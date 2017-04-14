<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>

import { default as generateColorScheme } from './helpers/color-scheme-generator'

export default {
  name: 'app',
  beforeMount () {
    const colorScheme = generateColorScheme()

    document.body.style.backgroundColor = colorScheme.strong1
    document.body.style.color = colorScheme.pastel1
  }
}
</script>

<style lang="scss">

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  max-width: 1200px;
  margin: 0 auto;
  margin-top: 42px;
}
</style>
