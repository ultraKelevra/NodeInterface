<template>
  <transition name="fade" appear>
    <div class="node"
         :class="{dragged:dragged}"
         :style="{left: offset.x+'px', top: offset.y+'px'}">
      <div class="node-bar draggable-area"
           @click="OnClick">
        <span>{{ label }}</span>
        <styl-button material="transparent"
                     @btnClick.stop="OnDeleteNode">
          <icon-close></icon-close>
        </styl-button>
      </div>
      <div class="node-body">
        <div class="node-output-area">
          <ul>
            <node-output v-for="output in outputs"
                         :id="output.id"
                         :label="output.label"
                         @clickOutput="OnClickOutput"
                         @mouseenterOutput="OnMouseEnterOutput"
                         @mouseleaveOutput="OnMouseLeaveOutput"
                         :key="output.id">
            </node-output>
          </ul>
        </div>
        <!--<div class="node-form-area">-->
          <!--<form action="">-->
            <!--<input type="text">-->
          <!--</form>-->
          <!--balaclava-->
        <!--</div>-->
        <div class="node-input-area">
          <ul>
            <node-input v-for="input in inputs"
                        :id="input.id"
                        :label="input.label"
                        @clickInput="OnClickInput"
                        @mouseenterInput="OnMouseEnterInput"
                        @mouseleaveInput="OnMouseLeaveInput"
                        @disconnect="$emit('disconnect',$event)"
                        :key="input.id">
            </node-input>
          </ul>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  import NodeInput from './NodeInput';
  import NodeOutput from './NodeOutput';
  import StylButton from '../Button/StylButton';
  import StylForm from '../Form/StylForm';
  import Spiner from '../Misc/Spiner';
  import IconClose from '../Button/IconClose';

  export default {
    props: ['label', 'inputs', 'outputs'],
    data() {
      return {
        inputList: [],
        outputList: [],
        offset: {x: 0, y: 0},
        dragged: false
      };
    },
    methods: {
      OnClick(event) {
        event.node = this;
        this.$emit('dragUpdate', event);
      },
      OnClickInput(event) {
        event.node = this;
        this.$emit('clickInput', event);
      },
      OnMouseEnterInput(event) {
        event.node = this;
        this.$emit('mouseenterInput', event);
      },
      OnMouseLeaveInput(event) {
        event.node = this;
        this.$emit('mouseleaveInput', event);
      },
      OnClickOutput(event) {
        event.node = this;
        this.$emit('clickOutput', event);
      },
      OnMouseEnterOutput(event) {
        event.node = this;
        this.$emit('mouseenterOutput', event);
      },
      OnMouseLeaveOutput(event) {
        event.node = this;
        this.$emit('mouseleaveOutput', event);
      },
      OnDeleteNode() {
        this.inputList.map((input) => {
          if (input.connected) {
            let output = input.connectedOutput;
            output.connectedInputs = output.connectedInputs.filter((connectedInput) => {
              return connectedInput != input;
            });
          }
        });
        this.outputList.map((output) => {
          if (output.connectedInputs.length > 0)
            output.connectedInputs.map((connectedInput) => {
              connectedInput.connectedOutput = null;
              connectedInput.connected = false;
            });
        });
        this.$emit('deleteNode', this);
      },
      CalculateChildrenPosition() {
        this.inputList.map((elem) => {
          elem.CalculateGrabPosition();
        });
        this.outputList.map((elem) => {
          elem.CalculateGrabPosition();
        });
      }
    },
    components: {
      NodeInput,
      NodeOutput,
      StylButton,
      StylForm,
      Spiner,
      IconClose
    },
    mounted() {
      let position = this.$parent.$data.hotPosition;
      this.$el.style.left = (position.x - 15) + 'px';
      this.$el.style.top = (position.y - 15) + 'px';
      this.$parent.nodeReferences.push(this);
      this.$parent.GrabNode({node: this, x: position.x, y: position.y});
    }
  }
</script>

<style>
  .node {
    transform-origin: center;
    min-width: 100px;
    display: block;
    position: absolute;
    top: 50px;
    left: 30px;
    box-shadow: 0 2px 5px 0 rgba(0, 0, 0, .2);
    transition: box-shadow .2s, transform .2s;
    transform: scale(1);
  }

  .node.dragged {
    box-shadow: 0 15px 10px -5px rgba(0, 0, 0, .2);
    transform: scale(1.025);
    z-index: 1;
  }

  .node-bar {
    position: relative;
    display: flex;
    justify-content: space-between;
    background: rgba(100, 100, 100, .75);
    border-radius: 3px 3px 0 0;
    padding: 3px 3px 3px 10px;
    font-weight: bold;
    cursor: move;
  }

  .node-body {
    background: rgba(180, 180, 180, .75);
    border-radius: 0 0 3px 3px;
  }

  .node-output-area {
    text-align: right;
    padding: 5px 0 5px 15px;
  }

  .node-output-area ul,
  .node-input-area ul{
    display: flex;
    flex-direction: column;
  }

  .node-form-area {
    padding: 5px 15px;
  }

  .node-input-area {
    text-align: left;
    padding: 5px 15px 5px 0;
  }

  /*---------------------------------------------------------------------separar despues*/
  input {
    border: none;
    border-radius: 3px;
    color: rgb(50, 50, 50);
    font-size: 15px;
    padding: 2px 5px;
    box-shadow: inset 1px 1px 2px rgba(0, 0, 0, .2);
  }

</style>
