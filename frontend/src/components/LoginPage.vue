<template>
    <div id="login-container">
        <div class="login-components">
            <h1>Login</h1>
        </div>
        <div class="login-components">
            <form>
                <div>
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div>
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <div>
                    <button type="submit">Login</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
  name: 'LoginPage',
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