<template>
  <li class="node-output"
      :class="{connected:connected}"
      @click="OnClick"
      @mouseenter="OnMouseEnter"
      @mouseleave="OnMouseLeave">
    <span>{{ label }}</span>
    <!--<span>{{ connectedInputs.length }}</span>-->
    <!--<id-tag>{{ id }}</id-tag>-->
    <dot></dot>
  </li>
</template>

<script>
  import IdTag from '../Misc/IdTag'
  import Dot from '../Misc/Dot'

  export default {
    props: ['label'],
    data() {
      return {
        connectedInputs: [],
        grabPosition: {
          x: 0,
          y: 0
        },
      };
    },
    methods: {
      OnClick(event) {
        event.output = this;
        this.$emit('clickOutput', event);
      },
      OnMouseEnter(event) {
        event.output = this;
        this.$emit('mouseenterOutput', event);
      },
      OnMouseLeave(event) {
        event.output = this;
        this.$emit('mouseleaveOutput', event);
      },
      CalculateGrabPosition() {
        let boundRect = this.$el.getBoundingClientRect();
        this.grabPosition.x = boundRect.left + boundRect.width - 10.0;
        this.grabPosition.y = (boundRect.top + (boundRect.height / 2.0));
      }
    },
    computed: {
      connected() {
        return this.connectedInputs.length > 0;
      }
    },
    components: {
      IdTag,
      Dot
    },
    //hooks
    mounted() {
      this.CalculateGrabPosition();
      this.$parent.$data.outputList.push(this);
    }
  }
</script>

<style>
  .node-output {
    position: relative;
    display: inline-block;
    margin: 2px 0;
    padding: 0 5px;
    background: rgba(70, 70, 70, .75);
    border-radius: 3px 0 0 3px;
    text-align: left;
  }

  .node-output:hover {
    background: rgba(200, 200, 200, .75);
    color: rgb(80, 80, 80);
  }

</style>
