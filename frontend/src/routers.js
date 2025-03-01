import { createRouter, createWebHistory } from "vue-router";


import HelloWorld from "./components/HelloWorld.vue";
import LoginPage from "./components/LoginPage.vue";


const routes = [

    {
        name: "HelloWorld",
        component: HelloWorld,
        path: "/hello",
    },
    {
        name: "Login",
        component: LoginPage,
        path: "/login",
        

    }
]


const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;


