<template>
    <div>
        <h3>用户列表页</h3>
        <table border="2">
            <tr>
                <td>ID</td>
                <td>姓名</td>
                <td>年龄</td>
                <td>个人信息</td>
                <td>操作</td>
            </tr>
            <tr v-for="user in users" :key="user.id">
                <td>{{user.id}}</td>
                <td>{{user.name}}</td>
                <td>{{user.age}}</td>
                <td>{{user.content}}</td>
                <td><a href="javascript: void(0);" @click="del_user(user.id)">删除</a> | <router-link :to="`/detail/${user.id}`">查看详情</router-link></td>
            </tr>
        </table>
        <br>
        用 户 名：<input type="text" v-model="name"><br>
        年    龄：<input type="text" v-model="age"><br>
        个人信息：<input type="text" v-model="content"><br>
        <button @click="add_user">添加用户</button>
    </div>
</template>

<script>
export default {
    name: "User",
    data(){
        return{
            users: localStorage.users ? JSON.parse(localStorage.users) : [],
            name:'',
            age:"",
            content:"",
        }
    },
    methods:{
        add_user(){
            if (this.name && this.age && this.content){
                let user = {};
                if (this.users.length){
                    user['id'] = this.users[this.users.length - 1]['id'] + 1;
                }else {
                    user['id'] = 1;
                }
                user['name'] = this.name;
                user['age'] = this.age;
                user['content'] = this.content;
                this.users.push(user);
                localStorage.users = JSON.stringify(this.users);
                this.name = "";
                this.age = "";
                this.content = ""
            }
        },
        del_user(id){
            for (let i=0; i < this.users.length; i++){
                if (this.users[i]['id'] === id){
                    this.users.splice(i, 1);
                    break
                }
            }
            localStorage.users = JSON.stringify(this.users);
        },
    }

}
</script>

<style scoped>

</style>
