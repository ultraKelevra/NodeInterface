<template>
  <button class="btn"
          :class="{
          'btn-danger':type==='danger',
          'btn-warning':type==='warning',
          'btn-success':type==='success',
          'btn-primary':type==='primary',
          'btn-shadow':material==='solid',
          'btn-transparent':material==='transparent',
          'btn-text-shadow':text==='carved'}"
          @click="OnClick">
    <slot></slot>
  </button>
</template>

<script>
  export default {
    props: {'type': {default: 'default'}, 'material': {default: 'solid'}, 'text': {default: 'normal'}},
    methods: {
      OnClick(event) {
        this.$emit('click', event);
      }
    }
  }
</script>

<style>

  .btn {
    border: none;
    padding: 3px;
    border-radius: 3px;
    font-weight: bold;
    margin: 3px;
    transition: .1s;
    cursor: default;
    user-select: none;
    color: rgb(200, 200, 200);
    fill: rgb(200, 200, 200);
    stroke: rgb(200, 200, 200);
    font-size: calc(5px + 1vmin);
  }

  /*transparent-basic-text*/
  .btn.btn-transparent {
    color: rgb(150, 150, 150);
    fill: rgb(150, 150, 150);
    stroke: rgb(150, 150, 150);
  }

  /*background*/
  .btn:not(.btn-transparent) {
    background: rgb(100, 100, 100);
  }

  .btn:not(.btn-transparent):hover {
    background: rgb(150, 150, 150);
  }

  .btn.btn-transparent {
    background: transparent;
  }

  /*shadow*/
  .btn.btn-shadow {
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, .2);
  }

  .btn.btn-text-shadow {
    text-shadow: 0 -1px 0 rgba(0, 0, 0, .2);
  }

  /*text*/
  .btn.btn-primary {
    color: #47b9eb;
    fill: #47b9eb;
    stroke: #47b9eb;
  }

  .btn.btn-success {
    color: rgb(72, 255, 107);
    fill: rgb(72, 255, 107);
    stroke: rgb(72, 255, 107);
  }

  .btn.btn-warning {
    color: rgb(255, 255, 50);
    stroke: rgb(255, 255, 50);
    fill: rgb(255, 255, 50);
  }

  .btn.btn-danger {
    color: rgb(255, 89, 86);
    fill: rgb(255, 89, 86);
    stroke: rgb(255, 89, 86);
  }

  /*transparent:hover*/
  .btn.btn-transparent:hover {
    color: rgb(200, 200, 200);
    fill: rgb(200, 200, 200);
    stroke: rgb(200, 200, 200);
  }

  .btn.btn-transparent.btn-primary:hover {
    color: skyblue;
    fill: skyblue;
    stroke: skyblue;
  }

  .btn.btn-transparent.btn-success:hover {
    color: rgb(119, 255, 155);
    fill: rgb(119, 255, 155);
    stroke: rgb(119, 255, 155);
  }

  .btn.btn-transparent.btn-warning:hover {
    color: rgb(255, 254, 102);
    stroke: rgb(255, 254, 102);
    fill: rgb(255, 254, 102);
  }

  .btn.btn-transparent.btn-danger:hover {
    color: lightpink;
    fill: lightpink;
    stroke: lightpink;
  }

  /*solid:hover*/
  .btn:not(.btn-transparent):hover {
    color: rgb(50, 50, 50);
    fill: rgb(50, 50, 50);
    stroke: rgb(50, 50, 50);
  }

  .btn:not(.btn-transparent).btn-primary:hover {
    background: skyblue;
    color: rgb(100, 100, 100);
    fill: rgb(100, 100, 100);
    stroke: rgb(100, 100, 100);
  }

  .btn.btn-success:hover {
    background: rgb(119, 255, 155);
    color: rgb(100, 100, 100);
    fill: rgb(100, 100, 100);
    stroke: rgb(100, 100, 100);
  }

  .btn:not(.btn-transparent).btn-warning:hover {
    background: rgb(255, 254, 102);
    color: rgb(100, 100, 100);
    stroke: rgb(100, 100, 100);
    fill: rgb(100, 100, 100);
  }

  .btn:not(.btn-transparent).btn-danger:hover {
    background: lightpink;
    color: rgb(100, 100, 100);
    fill: rgb(100, 100, 100);
    stroke: rgb(100, 100, 100);
  }
</style>
