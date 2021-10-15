import { createStore } from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
const getAPI = axios.create({
  baseURL: 'http://127.0.0.1:5050/',
})
export default createStore({
  state: {
    accessToken: null,
    refreshToken: null,
    data: ''
  },
  plugins:
    [createPersistedState()],
  mutations: {
    updateStorage(state, { access, refresh }) {
      state.accessToken = access
      state.refreshToken = refresh
    }
  },
  getters: {
    loggedIn(state) {
      return state.accessToken != null
    }
  },
  actions: {
    userLogin(context, user) {
      return new Promise((resolve, reject) => {
        getAPI.post('api-token/', {
          username: user.username,
          password: user.password
        })
          .then(response => {
            context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh })
            console.log(this.accessToken)
            console.log(this.refreshToken)
            resolve()
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    userLogout(context) {
      if (context.getters.loggedIn) {
        context.commit('destroyToken')
      }
    }
  },
  modules: {
  }
})
