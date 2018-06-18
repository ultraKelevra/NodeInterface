<template>
  <transition name="fade" appear>
    <div class="node"
         :class="{dragged:dragged}"
         :style="{left: offset.x+'px', top: offset.y+'px'}">
      <div class="node-bar draggable-area"
           @click.stop="DragDrop">
        <span>{{ label }}</span>
        <span style="font-size: 20px; color: gray;">{{ id }}</span>
        <styl-button material="transparent"
                     @click.stop="Delete">
          <icon-close></icon-close>
        </styl-button>
      </div>
      <div class="node-body">
        <div class="node-output-area">
          <ul>
            <node-output v-for="output in node.outputs"
                         :output="output"
                         :key="output.id">
            </node-output>
          </ul>
        </div>
        <div class="node-input-area">
          <ul>
            <node-input v-for="input in node.inputs"
                        :input="input"
                        :key="input.id">
            </node-input>
          </ul>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  import {bus} from '../../main';
  import NodeInput from './NodeInput';
  import NodeOutput from './NodeOutput';
  import StylButton from '../Button/StylButton';
  import StylForm from '../Form/StylForm';
  import Spiner from '../Misc/Spiner';
  import IconClose from '../Button/IconClose';

  export default {
    props: ['node', 'mousePosition'],
    data() {
      return {
        inputList: [],
        outputList: [],
        dragOffset: {x: 0, y: 0},
        offset: {x: 150, y: 150},
        dragged: false
      };
    },
    computed: {
      id() {
        return this.node.id;
      },
      label() {
        return this.node.label;
      }
    },
    methods: {
      DragDrop(event) {
        let rect = this.$el.getBoundingClientRect();
        this.dragOffset.x = event.x - rect.left;
        this.dragOffset.y = event.y - rect.top;
        if (this.dragged) this.Drop();
        else
          this.Drag();
      },
      Drag() {
        this.dragged = true;
        this.UpdateNodePosition();
      },
      Drop() {
        this.dragged = false;
        this.UpdateNodePosition();
      },
      Delete() {
        bus.$emit('deleteNode', this)
      },
      UpdateNodePosition() {
        this.offset.x = this.mousePosition.x - this.dragOffset.x;
        this.offset.y = this.mousePosition.y - this.dragOffset.y;
        this.CalculateChildrenPositions();
        if (this.dragged)
          window.requestAnimationFrame(this.UpdateNodePosition);
      },
      CalculateChildrenPositions() {
        this.inputList.map((elem) => {
          elem.CalculateConnectionDrawPosition();
        });
        this.outputList.map((elem) => {
          elem.CalculateConnectionDrawPosition();
        });
      },
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
      this.dragOffset.x = 15;
      this.dragOffset.y = 10;
      this.Drag();
    }
  }
</script>

<style>
  .node {
    transform-origin: center;
    min-width: 100px;
    display: block;
    position: absolute;
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
  .node-input-area ul {
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
