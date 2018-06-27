<template>
  <form :id="form.id">
    <component v-for="(elem,index) in form.elements"
               :is="elem.type"
               :elem="elem"
               :id="form.id + '-'+index">
    </component>
    <!--<message-box :messages="['message-0','message-1','message-2']"></message-box>-->
  </form>
</template>

<script>
  import Slct from './Slct';
  import Txt from './Txt';
  import Num from './Num';
  import MessageBox from '../DragDropInterface/MessageBox/MessageBox';
  import Spiner from '../Misc/Spiner';
  import TableVisual from '../TableVisual';

  export default {
    props: ['form'],

    components: {
      Txt,
      Num,
      Slct,
      Spiner,
      MessageBox,
      TableVisual
    }
  }
</script>

<style>
  .mono-field {
    display: flex;
    flex-direction: column;
    margin: 5px 0;
    position: relative;
  }

  label {
    font-size: 17px;
    position: relative;
  }

  fieldset {
    border-radius: 3px;
    border: 1px solid lightgray;
    padding: 5px;
  }
</style>
