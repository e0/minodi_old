<template>
  <div class="home">
    <h1>minodi</h1>
    <hr>
    <h2>a web consulting agency, from design to production</h2>
    <h2>select what you need help with from the menu below and we will get started</h2>
    <hr>
    <h1>Menu</h1>
    <p class="subtitle">you can select any number of options from any category</p>
    <div v-for="section in sections" class="section">
      <h2>{{ section.title }}</h2>
      <span v-for="option in section.options" class="option">{{ option }}</span>
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
  name: 'home',
  data () {
    return {
      sections: [
        {
          title: 'design',
          options: [
            'Logo',
            'UI (User interface)',
            'UX (User interaction)'
          ]
        },
        {
          title: 'front-end development',
          options: [
            'HTML & CSS',
            'JavaScript',
            'AngularJS',
            'React',
            'Vue.js',
            'Elm'
          ]
        },
        {
          title: 'iOS & macOS',
          options: [
            'Objective-C',
            'Swift',
            'React',
            'RubyMotion'
          ]
        },
        {
          title: 'back-end development',
          options: [
            'Django (Python)',
            'Ruby on Rails',
            'Elixir',
            'PHP',
            'ASP.NET'
          ]
        },
        {
          title: 'database',
          options: [
            'PostgreSQL',
            'Microsoft SQL',
            'MySQL',
            'sqlite',
            'MongoDB',
            'RethinkDB',
            'Neo4j'
          ]
        },
        {
          title: 'server & automation',
          options: [
            'Ubuntu',
            'Red Hat',
            'Azure',
            'Windows Server',
            'Docker',
            'Jenkins',
            'Heroku'
          ]
        },
        {
          title: 'online payments',
          options: [
            'Stripe',
            'Paymill'
          ]
        },
        {
          title: 'social network integrations',
          options: [
            'Facebook',
            'LinkedIn',
            'Twitter'
          ]
        }
      ]
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
