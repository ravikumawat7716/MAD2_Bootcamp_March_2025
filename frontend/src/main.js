import { createApp } from 'vue'
import App from './App.vue'
import './style.css' 
import router from './routers'

const app = createApp(App)
app.use(router)

app.mount('#app');
