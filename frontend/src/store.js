import { createStore } from 'vuex'

// this.$store.state.prediction
const state = {
    prediction: []
            
     
}

// this.$store.commit('setPrediction', prediction)
const mutations = {
    setPrediction(state, prediction){
        state.prediction = prediction
    }
}

export default createStore({state, mutations})