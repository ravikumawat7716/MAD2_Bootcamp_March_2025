<template>
    <h2>Admin Dashboard</h2>
    <p v-if="username">Welcome, {{ username }}</p>

</template>


<script>
import axios from 'axios';
export default {
    name: 'Admindashboard',
    data() {
        return {
            username: '',
            token: ''
        }

    },
    async mounted() {
        this.token = localStorage.getItem('token');
        if (!this.token) {
            this.$router.push('/login');
        }
        else {
            try {
                const response = await axios.get('http://localhost:5000/admin', {
                    headers: {
                        Authorization: `Bearer ${this.token}`
                    }
                });
                console.log(response.data);
                this.username = response.data.username;
            } catch (error) {
                console.error(error);
                localStorage.removeItem('token');
                this.$router.push('/login');

            }
        }
    }
}



</script>