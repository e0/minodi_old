<template>
  <div class="home">
    <h1>minodi</h1>
    <hr>
    <h2>a web consulting agency, from design to production</h2>
    <h2>select the skills you need with and we will get started</h2>
    <hr>
    <div class="wrapper">
      <div v-for="section in sections" class="section">
        <h2>{{ section.title }}</h2>
        <p
          v-for="option in section.options"
          :class="{ selected: isSelected(section.title, option) }"
          @click="toggleSelection(section.title, option)"
          class="option"
        >{{ option }}</p>
      </div>
    </div>
    <hr>
    <div>
      <p>Happy with the selections? Fill in your contact details and click send. We will try to get back to you as soon as possible.</p>
      <form>
        <input type="text" placeholder="Name">
        <input type="phone" placeholder="Phone">
        <input type="email" placeholder="Email">
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
  },
  methods: {
    toggleSelection (section, option) {
      if (!(section in this.selections)) {
        this.selections[section] = [option]
      } else {
        if (this.selections[section].includes(option)) {
          const index = this.selections[section].indexOf(option)
          this.selections[section].splice(index, 1)
          if (this.selections[section].length === 0) {
            delete this.selections[section]
          }
        } else {
          this.selections[section].push(option)
        }
      }

      this.$forceUpdate()
    },
    isSelected (section, option) {
      return section in this.selections && this.selections[section].includes(option)
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

.wrapper {
  display: flex;
  flex-wrap: wrap;
}

.section {
  flex-grow: 1;
  width: calc(25% - 42px);
  margin: 21px;
  margin-bottom: 42px;

  .option {
    background-color: #f8f8f8;
    padding: 3px;
    user-select: none;

    &.selected {
      background-color: #80ca80;
      color: #f2fbf2;
    }
  }
}

form {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;

  input, a {
    flex-grow: 1;
    padding: 7px;
    box-sizing: border-box;
    background-color: #f8f8f8;
    border-radius: 0;
    height: 42px;
  }

  input {
    font-size: 21px;
    line-height: 28px;
    appearance: none;
    border: 1px solid #ccc;
    margin-right: 7px;

    &:focus {
      border: 1px solid #000;
      outline: none;
      outline-width: 0;
    }
  }

  a {
    color: #fefefe;
    background-color: #000;
    font-size: 21px;
    text-align: center;
    text-decoration: none;
  }
}

footer {
  margin-top: 63px;
  padding: 7px;
  margin-bottom: 0;
  text-align: center;
}

@media(hover: hover) {
  .option:hover {
    cursor: pointer;
    background-color: #80ca80;
    color: #f2fbf2;
  }
}

@media all and (max-width: 1024px) {
  .section {
    width: 100%;
    margin: 0;
  }

  form {
    display: flex;
    flex-wrap: wrap;

    input, a {
      width: 100%;
      margin: 7px 0;
    }
  }
}

</style>
