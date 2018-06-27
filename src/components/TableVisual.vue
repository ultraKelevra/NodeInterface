<template>
  <div class="table-container">
    <table>
      <thead>
      <tr>
        <th v-for="(header,key) in table[0]">{{key}}</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="row in table">
        <th v-for="cell in row">{{cell}}</th>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        table: {
          "0": {"alpha": 1, "beta": "uno", "gamma": "balaclava"},
          "1": {"alpha": 2, "beta": "due", "gamma": "rice"},
          "2": {"alpha": 3, "beta": "tre", "gamma": "rise"},
          "3": {"alpha": 4, "beta": "cuatro", "gamma": "arisen"}
        },
      };
    }
  }
</script>

<style>
  .table-container {
    position: relative;
    max-width: 500px;
    max-height: 500px;
    overflow: auto;
  }

  table {
    position: relative;
    border-spacing: 0;
    font-weight: normal !important;
  }

  thead th {
    padding: 3px 10px;
    font-weight: bold;
  }

  thead th:first-child {
    border-radius: 3px 0 0 0;
  }

  thead th:last-child {
    border-radius: 0 3px 0 0;
  }

  thead th:nth-child(even) {
    background: rgb(120, 120, 120);
  }

  thead th:nth-child(odd) {
    background: rgb(100, 100, 100);
  }

  tbody th:nth-child(even) {
    background: lightgray;
  }

  tbody th:nth-child(odd) {
    background: darkgray;
  }

  tbody th {
    padding: 0 5px;
    font-weight: normal;
    color: rgb(100, 100, 100);
  }

  tbody tr:hover th:nth-child(even) {
    background: rgb(235, 235, 235);
  }

  tbody tr:hover th:nth-child(odd) {
    background: rgb(190, 190, 190);
  }

  tbody tr:last-child th:first-child {
    border-radius: 0 0 0 3px;
  }

  tbody tr:last-child th:last-child {
    border-radius: 0 0 3px 0;
  }
</style>
