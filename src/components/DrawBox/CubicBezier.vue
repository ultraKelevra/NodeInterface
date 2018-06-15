<template>
  <path :fill="fill" :stroke="stroke" :stroke-width="strokeWidth" :d="d" stroke-linecap="round"></path>
</template>

<script>
  export default {
    props: ['start', 'end', 'fill', 'stroke', 'strokeWidth'],
    computed: {
      d() {
        let m = 'M' + this.start.x + ',' + this.start.y + ' ';
        let mid = Math.abs((this.end.x - this.start.x) / 2);
        let cVector1 = 'C' + (this.start.x + mid) + ',' + this.start.y + ' ';
        let cVector2 = (this.end.x - mid) + ',' + this.end.y + ' ';
        let cEnd = this.end.x + ',' + this.end.y;
        return m + cVector1 + cVector2 + cEnd;
      }
    }
  }
</script>

<style scoped>

</style>
