<template>
  <div id="app">
<!--    <img src="./assets/logo.png">-->
<!--    使用组件-->
<!--    <HelloWorld/>-->
    <First></First>
    <hr>
    <Second></Second>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld'
// 注册组件时组要先将组件导入过来
import First from "./components/First";
import Second from "./components/Second";

export default {
  name: 'App',
  components: {
    // 将组件注册到根组件中
    // HelloWorld
    First:First,
    Second:Second,
  }
}
</script>

<style>
/*#app {*/
/*  font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
/*  -webkit-font-smoothing: antialiased;*/
/*  -moz-osx-font-smoothing: grayscale;*/
/*  text-align: center;*/
/*  color: #2c3e50;*/
/*  margin-top: 60px;*/
/*}*/
</style>
