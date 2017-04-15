<template>
  <div class="home">
    <h1>minodi</h1>
    <hr>
    <h2>a web consulting agency, from design to production</h2>
    <h2>select what you need help with from the menu below and we will get started</h2>
    <hr>
    <h1>Menu</h1>
    <p class="subtitle">you can select any number of options from any category</p>
    <div class="section">
      <h2>1. design</h2>
      <span class="option">Logo</span>
      <span class="option">UI (User interface)</span>
      <span class="option">UX (User interaction)</span>
    </div>
    <div class="section">
      <h2>2. front-end development</h2>
      <span class="option">HTML & CSS</span>
      <span class="option">JavaScript</span>
      <span class="option">AngularJS</span>
      <span class="option">React</span>
      <span class="option">Vue.js</span>
      <span class="option">Elm</span>
      <span class="option">Mithril</span>
    </div>
    <div class="section">
      <h2>3. iOS & macOS</h2>
      <span class="option">Objective-C</span>
      <span class="option">Swift</span>
      <span class="option">React Native</span>
      <span class="option">RubyMotion</span>
    </div>
    <div class="section">
      <h2>4. back-end development</h2>
      <span class="option">Django (Python)</span>
      <span class="option">Ruby on Rails</span>
      <span class="option">Elixir</span>
      <span class="option">PHP</span>
      <span class="option">ASP.NET</span>
    </div>
    <div class="section">
      <h2>5. database</h2>
      <span class="option">PostgreSQL</span>
      <span class="option">Microsoft SQL</span>
      <span class="option">MySQL</span>
      <span class="option">sqlite</span>
      <span class="option">MongoDB</span>
      <span class="option">RethinkDB</span>
      <span class="option">Neo4j</span>
    </div>
    <div class="section">
      <h2>7. server & automation</h2>
      <span class="option">Ubuntu</span>
      <span class="option">Red Hat</span>
      <span class="option">Azure</span>
      <span class="option">Windows Server</span>
      <span class="option">Docker</span>
      <span class="option">Jenkins</span>
      <span class="option">Heroku</span>
    </div>
    <div class="section">
      <h2>8. online payments</h2>
      <span class="option">Stripe</span>
      <span class="option">Paymill</span>
    </div>
    <div class="section">
      <h2>9. social network integration</h2>
      <span class="option">Facebook</span>
      <span class="option">LinkedIn</span>
      <span class="option">Twitter</span>
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
export default {
  name: 'home'
}
</script>

<style lang="scss">

hr {
  color: #000;
  background-color: #000;
  height: 5px;
}

.section {
  margin-bottom: 42px;
}

.option, form input, form a {
  display: inline-block;
  width: calc(25% - 18px);
  cursor: pointer;
  margin: 7px;
  padding: 7px;
  text-align: center;
  border: 2px solid;
  box-sizing: border-box;
  border-radius: 0;
}

.option {
  font-size: 28px;

  &:hover {
    background-color: #acdfac;
  }
}

form {
  input {
    font-size: 21px;
    line-height: 28px;
  }

  a {
    color: #fefefe;
    background-color: #000;
    font-size: 28px;
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
  .option, form input, form a {
    display: block;
    width: 100%;
  }
}

</style>
