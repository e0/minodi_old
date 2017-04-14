<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>

import { default as generateColorScheme } from './helpers/color-scheme-generator'

export default {
  name: 'app',
  mounted () {
    const colorScheme = generateColorScheme()

    document.body.style.color = colorScheme.strong1
    document.body.style.backgroundColor = colorScheme.pastel1

    const boxes = document.getElementsByClassName('box')
    Array.from(boxes).forEach((box) => {
      box.style.color = colorScheme.strong2
      box.style.backgroundColor = colorScheme.pastel2
      box.style.border = `1px solid ${colorScheme.strong2}`
    })
  }
}
</script>

<style lang="scss">

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  max-width: 1200px;
  margin: 42px auto;
}

@media all and (max-width: 1024px) {
  #app {
    max-width: 100%;
    margin: 21px;
    p {
      font-size: 1.25em;
    }
  }
}
</style>
