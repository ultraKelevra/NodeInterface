<template>
  <!--<form>-->
    <!--<label for="000">{{  }}</label>-->
    <!--<input type="text" id="000">-->
    <!--&lt;!&ndash;<component v-for="(elem,index) in blueprint"&ndash;&gt;-->
               <!--&lt;!&ndash;:is="elem.type"&ndash;&gt;-->
               <!--&lt;!&ndash;:blueprint="elem"&ndash;&gt;-->
               <!--&lt;!&ndash;:compId="'node-'+formId+'-element-'+index+'-'+elem.type">&ndash;&gt;-->
    <!--&lt;!&ndash;</component>&ndash;&gt;-->
  <!--</form>-->
  <span>IMPLEMENT FORM!!!</span>
</template>

<script>
  import Slct from './Slct';
  import Txt from './Txt';
  import Num from './Num';

  export default {
    props: ['blueprint', 'formId'],
    components: {
      Txt,
      Num,
      Slct,
    }
  }
</script>

<style>

</style>
