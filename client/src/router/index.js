/*
* Copyright (c) 2018-2018 the ValueX authors
* All rights reserved.
*
* The project sponsor and lead author is Xu Rendong.
* E-mail: xrd@ustc.edu, QQ: 277195007, WeChat: ustc_xrd
* See the contributors file for names of other contributors.
*
* Commercial use of this code in source and binary forms is
* governed by a LGPL v3 license. You may get a copy from the
* root directory. Or else you should get a specific written 
* permission from the project author.
*
* Individual and educational use of this code in source and
* binary forms is governed by a 3-clause BSD license. You may
* get a copy from the root directory. Certainly welcome you
* to contribute code of all sorts.
*
* Be sure to retain the above copyright notice and conditions.
*/

import Vue from "vue";
import Router from "vue-router";

const routerOptions = [
    { path: "/", component: "Home" },
    { path: "/about", component: "About" },
    { path: "/example", component: "Example" },
    { path: "*", component: "Error" }
];

const routes = routerOptions.map(route => {
    return {
        ...route,
        component: () => import(`@/components/${route.component}.vue`)
    };
});

Vue.use(Router);

export default new Router({
    mode: "history",
    routes
});
