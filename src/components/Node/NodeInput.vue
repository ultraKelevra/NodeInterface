<template>
  <li class="node-input"
      :class="{connected:connected}"
      @click="OnClick"
      @mouseenter="OnMouseEnter"
      @mouseleave="OnMouseLeave">
    <span>{{ label }}</span>
    <!--<span>{{(connectedOutput!=null)?'y':'n' }}</span>-->
    <!--<id-tag>{{ id }}</id-tag>-->
    <dot></dot>
    <transition name="right" appear>
      <div v-if="showScissors"
           class="input-connection-cut-icon"
           @click.stop="OnScissorsClick">
        <icon-scisors></icon-scisors>
      </div>
    </transition>
  </li>
</template>

<script>
  import IdTag from '../Misc/IdTag';
  import StylButton from '../Button/StylButton';
  import IconScissors from '../Button/IconScissors';
  import Dot from '../Misc/Dot'

  export default {
    props: ['label'],
    data() {
      return {
        connectedOutput: null,
        connected: false,
        showScissors: false,
        grabPosition: {
          x: 0,
          y: 0
        },
      };
    },
    methods: {
      OnClick(event) {
        if (!this.connected) {
          event.input = this;
          this.$emit('clickInput', event);
        }
      },
      OnMouseEnter(event) {
        if (!this.connected) {
          event.input = this;
          this.$emit('mouseenterInput', event);
        }
        else {
          this.showScissors = true;
        }
      },
      OnMouseLeave(event) {
        if (!this.connected) {
          event.input = this;
          this.$emit('mouseleaveInput', event);
        }
        else {
          this.showScissors = false;
        }
      },
      CalculateGrabPosition() {
        let boundRect = this.$el.getBoundingClientRect();
        this.grabPosition.x = boundRect.left + 10.0;
        this.grabPosition.y = (boundRect.top + (boundRect.height / 2.0));
      },
      OnScissorsClick() {
        if (this.connected) {
          this.connected = false;

          this.connectedOutput = null;
          this.showScissors = false;
          this.$emit('disconnect', this);
        }
      },
      Disconnect() {
        let outputInputs = this.connectedOutput.connectedInputs;
        for (let i = 0; i < outputInputs.length; i++) {
          if (outputInputs[i] === this) {
            outputInputs.splice(i, 1);
            break;
          }
        }
        this.connectedOutput = null;
        this.connected = false;
        this.showScissors = false;
      }
    },
    components: {
      IdTag,
      StylButton,
      IconScisors: IconScissors,
      Dot
    },
    //hooks
    mounted() {
      this.CalculateGrabPosition();
      this.$parent.$data.inputList.push(this);
    }
  }
</script>

<style>
  .node-input {
    position: relative;
    display: inline-block;
    margin: 2px 0;
    padding: 0 5px;
    background: rgba(70, 70, 70, .75);
    border-radius: 0 3px 3px 0;
    text-align: left;
  }

  .node-input.connected {
    background: rgba(100, 100, 100, .75);
    color: rgb(230, 230, 230);
  }

  .node-input:not(.connected):hover {
    background: rgba(200, 200, 200, .75);
    color: rgb(80, 80, 80);
  }

  .node-input span {
    margin-left: 25px;
  }

  .node-input .input-connection-cut-icon {
    position: absolute;
    right: 100%;
    top: 0;
    height: 100%;
    left: -2.25vmin;
    fill: grey;
  }

  .node-input .input-connection-cut-icon:hover {
    fill: lightgrey;
  }
</style>
