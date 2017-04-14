<template>
  <div class="home">
    <h1>{{ msg }}</h1>
    <div class="box">
      <h2>Box</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      msg: 'Hello, how are you?'
    }
  }
}
</script>

<style lang="scss">

.box {
  padding: 42px;
  border-radius: 7px;
}

@media all and (max-width: 1024px) {
  .box {
    padding: 21px;
  }
}

</style>
