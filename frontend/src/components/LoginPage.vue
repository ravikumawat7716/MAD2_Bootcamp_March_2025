<template>
    <div id="login-container">
        <div class="login-components">
            <h1>Login</h1>
        </div>
        <div class="login-components">
            <form @submit.prevent="login">
                <div>
                    <label for="email">Email</label>
                    <input type="email" v-model="email" id="email" name="email" required>
                </div>
                <div>
                    <label for="password">Password</label>
                    <input type="password" v-model="password" id="password" name="password" required>
                </div>
                <div>
                    <button type="submit">Login</button>
                </div>
            </form>
        </div>
    </div>
</template>



<script>
import axios from 'axios';
export default {
  name: 'LoginPage',
    data() {
        return {
        email: '',
        password: ''
        }

    },
    methods: {
        async login() {
            if (this.email && this.password) {
                console.log(this.email, this.password);
            try {
                const response = await axios.post('http://localhost:5000/login', {
                    email: this.email,
                    password: this.password
                });
                console.log(response.data);
                const token = response.data.token;
                const role = response.data.role;
                // console.log(token);
                localStorage.setItem('token', token);
                localStorage.setItem('role', role);
                if (role === 'admin') {
                    this.$router.push('/admindashboard');
                } else {
                    this.$router.push('/userdashboard');
                }
            } catch (error) {
                console.error(error);
                alert
            }
        }
    }
    },
    mounted() {
        const token = localStorage.getItem('token');
        if (token) {
            this.$router.push('/userdashboard');
        }
    },

}


</script>







<style>
    #login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 500px;
        width: 360px;
        margin: 100px auto;
        background-color: #f8f5f5;
        border-radius: 10px;
        border: rgb(78, 78, 78) 1px solid;
        
    }



</style>