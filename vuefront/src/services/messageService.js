import api from '@/services/api'

export default {
  fetchmessages() {
    return api.get(`messages/`)
              .then(response => response.data)
  },
  postmessage(payload) {
    return api.post(`messages/`, payload)
              .then(response => response.data)
  },
  deletemessage(msgId) {
    return api.delete(`messages/${msgId}`)
              .then(response => response.data)
  }
}