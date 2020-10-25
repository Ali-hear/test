<template>
    <div>
        <h3>用户详情页</h3>
        <ul>
            <li>用户ID：{{user['id']}}</li>
            <li>用户名：{{user['name']}}</li>
            <li>生日：{{user['age']}}</li>
            <li>个人信息：{{user['content']}}</li>
        </ul>
    </div>
</template>

<script>
export default {
    name: "Detail",
    data: function () {
        let users = JSON.parse(localStorage.users);
        let user = {};
        let id = this.$route.params.id;
        for (let i=0; i < users.length; i++){
            if (parseInt(users[i]['id']) === parseInt(id)){
                user = users[i]
                break
            }
        }
        return {
            users: users,
            user: user,
        }
    }
}
</script>

<style scoped>

</style>
