<template>
    <div v-if="user">
        <h1>유저 상세 정보</h1>
        <p>아이디: {{ user.id }} </p>
        <p>비밀번호: {{ user.password }} </p>
        <p>이름: {{ user.name }} </p>
        <p>실시간 적용 확인 호잇</p>
    </div>
    <div v-else>
        <h1> 존재하지 않는 유저입니다. </h1>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: null
        }
    },
    created() {
        var id = this.$route.params.id

        this.$http.get(`/api/users/${id}`)
        .then((res) => {
            const user = res.data.user;
            if (user) this.user = user;
        })
        .catch((err) => {
            console.error(err);
        });
    }
}
</script>

<style>
</style>