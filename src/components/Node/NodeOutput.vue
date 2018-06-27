<template>
  <li class="node-output"
      @click.stop="OnClick"
      @mouseenter="OnMouseEnter"
      @mouseleave="OnMouseLeave">
    <span>{{ label }}</span>
    <dot></dot>
  </li>
</template>

<script>

  import {bus} from '../../main';
  import IdTag from '../Misc/IdTag';
  import Dot from '../Misc/Dot';

  export default {
    props: ['output'],
    data() {
      return {
        dragPosition: {
          x: 0,
          y: 0
        },
      };
    },
    computed: {
      id() {
        return this.output.id;
      },
      label() {
        return this.output.label;
      }
    },
    methods: {
      OnClick() {
        bus.$emit('outputClick', this);
      }
      ,
      OnMouseEnter() {
        bus.$emit('outputEnter', this);
      }
      ,
      OnMouseLeave() {
        bus.$emit('outputLeave', this);
      }
      ,
      CalculateConnectionDrawPosition() {
        let boundRect = this.$el.getBoundingClientRect();
        boundRect.x += window.scrollX;
        boundRect.y += window.scrollY;
        this.dragPosition.x = boundRect.left + boundRect.width - 10.0;
        this.dragPosition.y = (boundRect.top + (boundRect.height / 2.0));
      }
    }
    ,
    components: {
      IdTag,
      Dot
    }
    ,
    mounted() {
      this.CalculateConnectionDrawPosition();
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
