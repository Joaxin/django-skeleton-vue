import api from "@/services/api";

export default {
  fetchMessages() {
    return api.get(`messages/`).then(response => response.data);
  },
  postMessage(payload) {
    return api.post(`messages/`, payload).then(response => response.data);
  },
  // Django can't redirect to the slash URL while maintaining PATCH data. 
  // Change your form to point to localhost:8000/api/messages/74/ (note the trailing slash), 
  // or set APPEND_SLASH=False in your Django settings.
  patchMessage(msgId, payload) {
    return api.patch(`messages/${msgId}/`, payload)
      .then(response => response.data)
      .catch(e => { console.log(e) })
  },
  deleteMessage(msgId) {
    return api.delete(`messages/${msgId}`).then(response => response.data);
  },
  fetchCategory() {
    return api.get(`category/`).then(response => response.data);
  },
};
