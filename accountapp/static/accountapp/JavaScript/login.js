
function setCookie(name, value, options = {}) {

  options = {
    path: '/',
    // 필요한 경우, 옵션 기본값을 설정할 수도 있습니다.
    ...options
  };

  if (options.expires instanceof Date) {
    options.expires = options.expires.toUTCString();
  }

  let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

  for (let optionKey in options) {
    updatedCookie += "; " + optionKey;
    let optionValue = options[optionKey];
    if (optionValue !== true) {
      updatedCookie += "=" + optionValue;
    }
  }

  document.cookie = updatedCookie;
}


function send_input() {
    axios.post('/accounts/login/', {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value,
    })
      .then(function (response) {
        // handle success
        console.log(response);

        // Get token and generate cookies
        setCookie('drf_token', 'Token ' + response.data['token']);

        // redirect success_url
        window.location.href = '/accounts/hello_world_template/';

      })
      .catch(function (error) {
      // handle failure
        console.log(error);

        document.getElementById('alert_box').innerHTML
                 += "<div class='btn btn-danger rounded-pill px-5 mb-3'> 로그인을 실패했습니다. </div>";
      });
}