<template>
    <div>
        <h3>这是留言板</h3>
        <input type="text" v-model="msg">
        <input type="button" value="发表留言" @click="add_note">
        <ul>
            <li v-for="(note,index) in msg_list" :key="index">
                <span>{{ note }}</span>
                <a href="javascript:void(0)" @click="delNote(index)">删除</a>
            </li>
        </ul>
        <span>留言总数量：{{ msg_list.length }}条</span><br>
        <input type="button" value="删除所有留言" v-if="msg_list.length" @click="del_all">
    </div>
</template>

<script>
export default {
    name: "Home",
    data:function () {
        return {
            msg: "",
            // 判断msgs是否有值，有则显示，无则显示空列表
            msg_list:localStorage.msgs ? JSON.parse(localStorage.msgs): [],
        }
    },
    methods: {
        add_note() {
            let msg = this.msg;
            if (msg) {
                // 添加到末尾:push,添加到行首:unshift
                this.msg_list.unshift(this.msg);
                localStorage.msgs = JSON.stringify(this.msg_list);
                this.msg = '';
            } else {
                alert('留言不能为空！')
            }
        },
        delNote(index){
            this.msg_list.splice(index,1);

        },
        del_all(){
            this.msg_list.splice(0,this.msg_list.length);
            localStorage.removeItem("msgs")
        },
    }
}
</script>

<style scoped>

</style>
