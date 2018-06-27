<template>
  <div class="message-box"
       :class="{'unfolded':unfolded}">
    <btn class="message-box-btn"
         material="flat"
         @click="unfolded=!unfolded">Log
    </btn>
    <div class="message-container">
      <message v-for="(message,index) in messages"
               :message="message">
      </message>
    </div>
  </div>
</template>

<script>
  import {bus} from '../../../main';
  import Message from './Message';
  import Btn from '../../Form/Btn';

  export default {
    data() {
      return {
        messages: [],
        unfolded: false,
        scrolling: false,
      }
    },
    components: {
      Message,
      Btn
    },
    mounted() {
      bus.$on('response', response => {
        this.messages.push(response);
      });
    }
  }
</script>

<style>
  .message-box {
    right: 5px;
    bottom: 5px;
    position: fixed;
    transform: translateX(102%);
    transition: .2s;
    width: 200px;
    height: 300px;
    background: rgb(70, 70, 70);
    border-radius: 3px;
  }

  .message-container {
    overflow: auto;
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    display: flex;
    flex-direction: column;
  }

  .message-box.unfolded {
    transform: translateX(0);
  }

  .message-box-btn {
    position: absolute;
    right: 100%;
    bottom: 0;
    margin-bottom: 0;
    margin-right: 5px;
  }
</style>
