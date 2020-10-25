<!--组件的template，内部只能有一个根标签-->
<template>
  <div>
    这是我的第一个组件===>组件使用成功
    <br>
    <span>这是阿黎啊</span>
    <h3>这还是h3</h3>
  </div>

</template>
<!--编写js代码的地方，当前对象就是组件对象-->
<script>
// 将组件导出
export default {
name: "First"
}
</script>

<!--当前组件的样式，scoped：脚手架提供的属性，
加上此属性代表当前样式只在当前组件中生效-->
<style scoped>
  div{
    color: aqua;
  }
  span{
    color: aquamarine;
  }
</style>
