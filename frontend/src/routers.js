import { createRouter, createWebHistory } from "vue-router";


import HelloWorld from "./components/HelloWorld.vue";
import LoginPage from "./components/LoginPage.vue";
import Userdashboard from "./components/Userdashboard.vue";


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
        

    },
    {
        name: "Userdashboard",
        component: Userdashboard,
        path: "/userdashboard",
    }
]


const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;


