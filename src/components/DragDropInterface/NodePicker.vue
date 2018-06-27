<template>
  <div class="node-picker"
       :class="{unfolded:unfolded}">
    <styl-button material="transparent"
                 @click.stop="unfolded=true">
      <icon-burger></icon-burger>
    </styl-button>
    <div class="picker-body">
      <div style="position: absolute; right: 0; top: 0;">
        <styl-button material="transparent"
                     @click.stop="unfolded=false">
          <icon-close class="small"></icon-close>
        </styl-button>
      </div>
      <styl-button v-for="(blueprint, index) in nodeBlueprints"
                   @click.stop="OnButtonClick(index)"
                   :key="index">
        {{ blueprint.label }}
      </styl-button>
    </div>
  </div>
</template>

<script>
  import {bus} from '../../main';
  import StylButton from '../Form/Btn';
  import IconClose from '../Form/IconClose';
  import IconBurger from '../Form/IconBurger';
  import Spiner from '../Misc/Spiner';


  export default {
    data() {
      return {
        nodeLabels: ['A', 'B', 'C'],
        unfolded: true,
        // nodeBlueprints: [],
        nodeBlueprints: [
          {
            'label': 'Table',
            'form': [
              {
                'type': 'TableVisual',
                'label': ''
              }
            ],
            'inputs': [{'label': 'TableIn'}],
            'outputs': [],
          }
        ],
        updated: false,
      }
    },
    methods: {
      OnButtonClick(index) {
        this.$store.dispatch('createNode', this.nodeBlueprints[index]);
        this.$http.post('/newnode/', {'code': index})
          .then(response => {
            bus.$emit('response',response);
          });
      },
      GetBlueprints() {
        this.$http.get('/blueprints/')
          .then(response => response.json())
          .then(data => {
            this.nodeBlueprints = data;
            this.updated = true;
          });
      }
    },
    components: {
      StylButton,
      IconClose,
      IconBurger,
      Spiner
    },
    mounted() {
      this.GetBlueprints();
    }
  }
</script>

<style>
  .node-picker {
    position: fixed;
    top: 0;
    left: 0;
  }

  .picker-body {
    position: absolute;
    top: 0;
    display: flex;
    background: rgb(70, 70, 70);
    flex-direction: column;
    width: 10vw;
    height: 100vh;
    transform: translateX(-100%);
    transition: .2s ease-in-out;
    padding: 35px 15px;
    box-shadow: 3px 0 3px 0 rgba(0, 0, 0, .2);
  }

  .node-picker.unfolded .picker-body {
    transform: translateX(0);
  }
</style>
