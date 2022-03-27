<template>
    <div class="users">
        <div v-for="(user, index) in users" :key="index" class="user">
            <h2>접속한 유저 {{ index+1 }}</h2>
            <p>아이디: {{ user.id }} </p>
            <p>이름: {{ user.name }} </p>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            users: []
        };
    },
    created() {
        this.$http.get('/api/users')
        .then((res) => {
            this.users = res.data.users;
        })
        .catch((err) => {
            console.error(err);
        });
    }
}
</script>

<style>
    .user {
        float: left;
        border: 2px solid black;
        padding: 15px;
        margin: 20px;
    }

</style>