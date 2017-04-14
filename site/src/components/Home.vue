<template>
  <div class="home">
    <h1>{{ msg }}</h1>
    <div class="box">
      <h2>Blizzard</h2>
      <p>sometimes there is a blizzard, sometimes you don't</p>
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
}

</style>
