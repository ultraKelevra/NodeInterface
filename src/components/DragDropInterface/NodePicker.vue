<template>
  <div class="node-picker"
       :class="{unfolded:unfolded}">
    <styl-button material="transparent"
                 @click.stop="unfolded=true">
      <icon-burger></icon-burger>
    </styl-button>
    <div class="picker-body">
      <div style="position: absolute; right: 0; top: 0;">
        <styl-button material="transparent"
                     @click.stop="unfolded=false">
          <icon-close></icon-close>
        </styl-button>
      </div>
      <styl-button v-for="(label,index) in nodeLabels"
                   @click.stop="OnButtonClick()"
                   :key="index">
        {{ label }}
        {{index}}
      </styl-button>
    </div>
  </div>
</template>

<script>
  import StylButton from '../Button/StylButton';
  import IconClose from '../Button/IconClose';
  import IconBurger from '../Button/IconBurger';


  export default {
    data() {
      return {
        nodeLabels: ['A', 'B', 'C'],
        unfolded: true,
        node: {
          label: 'A',
          inputs: [{label: 'IA'}],
          outputs: [{label: 'OA'}],
        },
      }
    },
    methods: {
      OnButtonClick() {
        this.$store.dispatch('createNode', this.node);
      }
    },
    components: {
      StylButton,
      IconClose,
      IconBurger
    }
  }
</script>

<style>
  .node-picker {
    position: fixed;
    top: 0;
    left: 0;
  }

  .picker-body {
    position: absolute;
    top: 0;
    display: flex;
    background: rgb(70, 70, 70);
    flex-direction: column;
    width: 10vw;
    height: 100vh;
    transform: translateX(-100%);
    transition: .2s ease-in-out;
    padding: 35px 15px;
    box-shadow: 3px 0 3px 0 rgba(0, 0, 0, .2);
  }

  .node-picker.unfolded .picker-body {
    transform: translateX(0);
  }
</style>
