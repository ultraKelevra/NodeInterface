<template>
  <transition name="bottom" appear>
    <div class="message"
         :class="{
          'success':message.status===200,
          'danger':message.status!==200
       }">
      <p>{{message.body}}</p>
      <p>{{message.status}}-{{message.statusText}}</p>
    </div>
  </transition>
</template>

<script>
  export default {
    props: ['message']
  }
</script>

<style>
  .message {
    background: lightgray;
    color: rgb(60, 60, 60);
    border-radius: 3px;
    padding: 5px;
    margin: 5px 5px 0 5px;
  }

  .message p:first-child {
    font-weight: normal;
    font-size: 15px;
    font-style: italic;
  }

  .message p:last-child {
    font-weight: bold;
    font-size: 20px;
  }

  .message.danger {
    background: rgb(227, 119, 107);
  }

  .message.success {
    background: #87ffb8;
  }
</style>
