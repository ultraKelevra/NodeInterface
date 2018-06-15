<template>
  <div class="drag-box"
       @mousemove="OnMouseMove"
       @click="Deselect">
    <draw-box :connections="connections">
    </draw-box>
    <node v-for="(node,index) in nodes"
          :label="node.label"
          :inputs="node.inputs"
          :outputs="node.outputs"
          @dragUpdate.stop="OnDragUpdate"
          @clickInput.stop="OnClickInput"
          @mouseenterInput.stop="OnMouseEnterInput"
          @mouseleaveInput.stop="OnMouseLeaveInput"
          @clickOutput.stop="OnClickOutput"
          @mouseenterOutput.stop="OnMouseEnterOutput"
          @mouseleaveOutput.stop="OnMouseLeaveOutput"
          @deleteNode="OnDeleteNode($event,index)"
          @disconnect="Disconnect"
          :key="node.id">
    </node>
    <node-picker :nodeLabels="nodeLabels"
                 @createNode="CreateNode">
    </node-picker>
  </div>
</template>

<script>
  import Node from '../Node/Node.vue';
  import DrawBox from '../DrawBox/DrawBox';
  import NodePicker from './NodePicker';

  export default {
    props: ['nodeLabels'],
    data() {
      return {
        //nodeGeneration
        nodes: [],
        nextNodeId: 0,
        nodeReferences: [],
        //draggingNode nodes
        nodeInitialOffset: {x: 0, y: 0},
        draggingNode: false,
        draggedNode: null,
        //draggingInputs/Outputs
        draggingInput: false,
        draggingOutput: false,
        draggedElement: null,
        draggedElementNode: null,
        //connections
        connections: [],
        hotConnection: {start: null, end: null, input: null, output: null},
        hotPosition: {x: 0, y: 0},
      }
        ;
    },
    methods: {
      //NodePicker
      CreateNode(code) {
        let newNode = {
          code: code,
          label: 'code',
          id: this.nextNodeId,
          inputs: [{label: 'A'}, {label: 'B'}, {label: 'C'}],
          outputs:
            [{label: 'out'}],
        };
        this.nextNodeId++;
        this.nodes.push(newNode);
      },
      //Node
      OnDeleteNode(node, index) {
        this.connections = this.connections.filter((elem) => {
          return elem.input.$parent !== node && elem.output.$parent !== node;
        });
        this.nodes.splice(index, 1);
      },
      Deselect() {
        this.DropNode();
        this.DropInputOutput();
      },
      OnMouseMove(event) {
        if (this.draggingNode) {
          let posX = event.clientX - this.nodeInitialOffset.x;
          let posY = event.clientY - this.nodeInitialOffset.y;

          if (posX < 0)
            posX = 0;
          if (posY < 0)
            posY = 0;

          this.draggedNode.offset.x = posX;
          this.draggedNode.offset.y = posY;
          this.draggedNode.CalculateChildrenPosition();
        }
        this.hotPosition.x = event.x;
        this.hotPosition.y = event.y;
      },
      OnDragUpdate(event) {
        if (this.draggingNode) {
          if (this.draggedNode === event.node)
            this.DropNode();
        }
        else if (!this.draggingOutput && !this.draggingInput)
          this.GrabNode(event);
      },
      GrabNode(event) {
        this.draggingNode = true;
        this.draggedNode = event.node;
        let boundRect = event.node.$el.getBoundingClientRect();
        this.nodeInitialOffset.x = event.x - boundRect.left;
        this.nodeInitialOffset.y = event.y - boundRect.top;
        this.draggedNode.dragged = true;
      },
      DropNode() {
        if (this.draggingNode) {
          this.draggingNode = false;
          this.draggedNode.$data.dragged = false;
          this.draggedNode.CalculateChildrenPosition();
        }
      },
      //Input/Output
      OnClickInput(event) {
        if (!this.draggingNode) {
          if (this.draggingOutput)
            this.Connect(event.input, this.draggedElement);
          else if (!this.draggingInput)
            this.DragInput(event.input);
        }
      },
      OnMouseEnterInput(event) {
        if (this.draggingOutput)
          this.Visualize(event.input, this.draggedElement);
      },
      OnMouseLeaveInput(event) {
        if (this.draggingOutput)
          this.Unvisualize(event.input, this.draggedElement);
      },
      OnClickOutput(event) {
        if (!this.draggingNode) {
          if (this.draggingInput)
            this.Connect(this.draggedElement, event.output);
          else if (!this.draggingOutput)
            this.DragOutput(event.output);
        }
      },
      OnMouseEnterOutput(event) {
        if (this.draggingInput)
          this.Visualize(this.draggedElement, event.output);
      },
      OnMouseLeaveOutput(event) {
        if (this.draggingInput)
          this.Unvisualize(this.draggedElement, event.output);
      },
      //actions
      DragInput(input) {
        this.draggingInput = true;
        this.draggedElement = input;
        this.hotConnection.start = this.hotPosition;
        this.hotConnection.end = input.grabPosition;
        this.connections.push(this.hotConnection);
      },
      DragOutput(output) {
        this.draggingOutput = true;
        this.draggedElement = output;
        this.hotConnection.start = output.grabPosition;
        this.hotConnection.end = this.hotPosition;
        this.connections.push(this.hotConnection);
      },
      DropInputOutput() {
        this.hotConnection = {start: null, end: null};
        if (this.draggingInput || this.draggingOutput) {
          this.draggingInput = false;
          this.draggingOutput = false;
          this.connections.pop();
          //this.hotConnection = {start: null, end: null};
        }
      },
      Visualize(input, output) {
        console.log('visualize');
        if (this.draggingInput) {
          this.hotConnection.start = output.grabPosition;
        } else
          this.hotConnection.end = input.grabPosition;
      },
      Unvisualize() {
        if (this.draggingInput)
          this.hotConnection.start = this.hotPosition;
        else
          this.hotConnection.end = this.hotPosition;
      },
      Connect(input, output) {
        input.$data.connectedOutput = output;
        output.$data.connectedInputs.push(input);
        input.$data.connected = true;
        this.draggingInput = false;
        this.draggingOutput = false;
        this.hotConnection.input = input;
        this.hotConnection.output = output;
        this.hotConnection = {start: null, end: null};
      },
      Disconnect(input) {
        for (let i = 0; i < this.connections.length; i++) {
          if (this.connections[i].input === input) {
            this.connections.splice(i, 1);
            break;
          }
        }
      }
    },
    components: {
      Node,
      DrawBox,
      NodePicker
    }
  }
</script>

<style>
  .drag-box {
    width: 100vw;
    height: 100vh;
  }
</style>
