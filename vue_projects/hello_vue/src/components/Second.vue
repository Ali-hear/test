<template>
  <div>
    <p>这是我的第二个组件</p>
    <h3>{{username}}</h3>
    <span @click="change">{{number}}</span>
  </div>
</template>

<script>
export default {
  name: "second",
  data:function (){
    return{
      username:'ali',
      number:50,
    }
  },
  methods:{
    change(){
      this.number-=3;
    }
  }
}
</script>

<style scoped>

</style>
