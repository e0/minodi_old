<template>
  <div class="home">
    <h1>minodi</h1>
    <hr>
    <h2>a web consulting agency, from design to production</h2>
    <h2>select the skills you need with and we will get started</h2>
    <hr>
    <div v-for="section in sections" class="section">
      <h2>{{ section.title }}</h2>
      <p v-for="option in section.options" class="option">{{ option }}</p>
    </div>
    <hr>
    <div>
      <p>Happy with the selections? Fill in your contact details and click send to get started.</p>
      <form>
        <input type="text" placeholder="name">
        <input type="phone" placeholder="phone">
        <input type="email" placeholder="email">
        <a class="button" href="#">Send</a>
      </form>
    </div>
    <footer>
      <p>minodi.com</p>
    </footer>
  </div>
</template>

<script>

import skills from '../skills'

export default {
  name: 'home',
  data () {
    return {
      selections: {},
      sections: skills
    }
  }
}
</script>

<style lang="scss">

hr {
  color: #000;
  background-color: #000;
  height: 5px;
}

.section {
  display: inline-block;
  width: calc(25% - 14px);
  padding: 7px;
  margin-bottom: 42px;

  .option {
    background-color: #f8f8f8;

    &:hover {
      cursor: pointer;
      background-color: #acdfac;
    }
  }
}

form {
  input, a {
    display: inline-block;
    width: calc(25% - 18px);
    margin: 7px;
    padding: 7px;
    border: 2px solid;
    box-sizing: border-box;
    border-radius: 0;
  }

  input {
    font-size: 21px;
    line-height: 28px;
  }

  a {
    color: #fefefe;
    background-color: #000;
    font-size: 28px;
    text-align: center;
    line-height: 32px;
    text-decoration: none;
  }
}

footer {
  margin-top: 63px;
  padding: 7px;
  margin-bottom: 0;
  text-align: center;
}

@media all and (max-width: 1024px) {
  .section {
    padding: 0;
  }
  .section, form input, form a {
    display: block;
    width: 100%;
    margin: 0 0 7px 0;
  }
}

</style>
