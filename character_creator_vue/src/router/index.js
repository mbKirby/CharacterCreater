import { createRouter, createWebHistory } from 'vue-router'
import CharacterCreation from '../views/CharacterCreation.vue'
import Login from '../views/Login.vue'
import Logout from '../views/Logout.vue'
import CharacterSheet from '../views/CharacterSheet.vue'

const routes = [
  {
    path: '/',
    name: 'CharacterCreation',
    component: CharacterCreation,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/logout',
    name: 'logout',
    component: Logout
  },
  {
    path: '/character-sheet',
    name: 'character-sheet',
    component: CharacterSheet
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
