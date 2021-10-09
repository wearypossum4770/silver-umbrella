import Vue from "vue";
import VueRouter from "vue-router";
/**Views */
import User from "@/views/User.vue";
import Profile from "@/views/Profile.vue";
import Blog from "@/views/Blog.vue";
import Chat from "@/views/Chat.vue";
import Home from "@/views/Home.vue";
import TodoList from "@/views/TodoList.vue";
import Weather from "@/views/Weather.vue";
import Postal from "@/views/Postal.vue";
import PostalMobile from "@/views/PostalMobile.vue";
import Quiz from '@/components/quiz/Quiz.vue';

/**Components */
import PLUCodes from "@/components/cashier/PLUCodes.vue";
import SignUpForm from "@/components/SignUpForm.vue";
import LoginForm from "@/components/LoginForm.vue";
import UserBoard from "@/components/UserBoard.vue";
import Checkout from "@/components/Checkout.vue";
Vue.use(VueRouter);

const routes = [
  {
    path:"/quiz",
    component:Quiz,
    name:"Quiz",
  },
  {
    path: "/cashier",
    component: PLUCodes,
    name: "PLUCodes",
  },
  {
    path: "/postal",
    component: Postal,
    name: "Postal",
  },
  {
    path: "/postal_mobile",
    component: PostalMobile,
    name: "PostalMobile",
  },
  {
    path: "/weather",
    component: Weather,
    name: "Weather",
  },
  {
    path: "/checkout",
    name: "Checkout",
    component: Checkout,
  },
  {
    path: "/chat",
    name: "Chat",
    component: Chat,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: UserBoard,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/blog",
    component: Blog,
    name: "Blog",
    meta: {
      guest: true,
    },
  },
  {
    path: "/login",
    component: LoginForm,
    name: "LoginForm",
    meta: {
      guest: true,
    },
  },
  {
    path: "/user/:id",
    component: User,
    children: [
      {
        path: "Profile",
        component: Profile,
      },
    ],
  },
  {
    path: "/todo",
    name: "TodoList",
    component: TodoList,
  },
  {
    path: "/register",
    name: "Registration",
    component: SignUpForm,
    meta: {
      guest: true,
    },
  },
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      guest: true,
    },
  },
  {
    path: "/about",
    name: "About",
    meta: {
      guest: true,
    },
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
