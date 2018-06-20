<template>
  <div class="drag-box"
       @mousemove="UpdateMousePosition">
    <draw-box :connections="connections"
              @drop="Drop">
    </draw-box>
    <node v-for="node in nodes"
          :node="node"
          :mousePosition="mousePosition"
          :key="node.id">
    </node>
    <node-picker></node-picker>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex';
  import {bus} from '../../main';
  import Node from '../Node/Node.vue';
  import DrawBox from './ConnectionsDrawBox';
  import NodePicker from './NodePicker';

  export default {
    data() {
      return {
        mousePosition: {x: 0, y: 0},

        //visual connections
        inPreview: false,
        connections: [],
        draggingInput: false,
        draggingOutput: false,
        hotConnection: {
          input: null,
          output: null,
          inputObj: null,
          outputObj: null
        },
      };
    },
    computed: {
      ...mapGetters(['nodes']),
    },
    methods: {
      UpdateMousePosition(event) {
        this.mousePosition.x = event.pageX;
        this.mousePosition.y = event.pageY;
      },
      //visual
      DragInput(input) {
        this.hotConnection.output = this.mousePosition;
        this.hotConnection.input = input.dragPosition;
        this.hotConnection.inputObj = input.$props.input;
        this.connections.push(this.hotConnection);
        this.draggingInput = true;
      },
      DragOutput(output) {
        this.draggingOutput = true;
        this.hotConnection.output = output.dragPosition;
        this.hotConnection.input = this.mousePosition;
        this.hotConnection.outputObj = output.$props.output;
        this.connections.push(this.hotConnection);
      },
      Drop() {
        if (this.draggingOutput || this.draggingInput) {
          this.draggingOutput = false;
          this.draggingInput = false;
          this.connections.pop();
        }
      },
      Preview(elem) {
        this.inPreview = true;
        if (this.draggingInput) {
          this.hotConnection.output = elem.dragPosition;
          this.hotConnection.outputObj = elem.$props.output;
        }
        else {
          this.hotConnection.input = elem.dragPosition;
          this.hotConnection.inputObj = elem.$props.input;
        }
      },
      Unpreview() {
        this.inPreview = false;
        if (this.draggingInput)
          this.hotConnection.output = this.mousePosition;
        else this.hotConnection.input = this.mousePosition;
      },
      Connect() {
        this.$store.dispatch('connect', {
          input: this.hotConnection.inputObj,
          output: this.hotConnection.outputObj
        });
        this.inPreview = false;
        this.draggingInput = false;
        this.draggingOutput = false;
        this.hotConnection = {
          input: null,
          output: null,
          inputObj: null,
          outputObj: null
        };
      },
      Disconnect(input) {
        this.$store.dispatch('disconnect', input.$props.input);
        let self = this;
        this.connections.map((obj, index) => {
          if (obj.inputObj === input.$props.input) {
            self.connections.splice(index, 1);
            return true;
          }
        });
      },
      DeleteNode(node) {
        this.connections = this.connections.filter(connection => {
          return connection.inputObj.node !== node.$props.node && connection.outputObj.node !== node.$props.node;
        });
        this.$store.dispatch('deleteNode', node.$props.node);
      },
    },
    components: {
      Node,
      DrawBox,
      NodePicker,
    },
    mounted() {
      bus.$on('inputClick', input => {
        if (this.draggingOutput)
          this.Connect();
        else if (!this.draggingInput)
          this.DragInput(input);
      });
      bus.$on('inputEnter', input => {
        if (this.draggingOutput)
          this.Preview(input);
      });
      bus.$on('inputLeave', input => {
        if (this.inPreview && this.draggingOutput)
          this.Unpreview();
      });
      bus.$on('outputClick', output => {
        if (this.draggingInput)
          this.Connect();
        else if (!this.draggingOutput)
          this.DragOutput(output);
      });
      bus.$on('outputEnter', output => {
        if (this.draggingInput)
          this.Preview(output);
      });
      bus.$on('outputLeave', output => {
        if (this.inPreview && this.draggingInput)
          this.Unpreview();
      });
      bus.$on('inputDisconnect', input => {
        this.Disconnect(input);
      });
      bus.$on('deleteNode', node => {
        this.DeleteNode(node);
      });
    }
  }
</script>

<style>
  .drag-box {
    /*position: absolute;*/
    /*width: 100vh;*/
    /*height: 100vh;*/
  }
</style>
