export default function({ rootGetters, commit, getters }, PAYLOAD) {
  let xhr = new XMLHttpRequest();
  let promise = new Promise((resolve, reject) => {
    xhr.open(
      "POST",
      rootGetters.endpoints("BASE") + rootGetters.endpoints("GET_USER")
    );
    xhr.setRequestHeader("Content-Type", "Application/json");
    xhr.setRequestHeader(
      "Authorization",
      "Bearer " + getters["get_accessToken"]
    );
    xhr.onload = () => {
      resolve(xhr);
    };
    xhr.onerror = () => {
      reject(xhr);
    };
    xhr.send(JSON.stringify(PAYLOAD));
  });
  promise.then((data) => {
    console.log(data.response);
    if (data.status == 200) {
      commit("set_user_if_loaded", true);
    } else {
      commit("set_user_if_loaded", false);
    }
  });
  return promise;
}
