
function send_input() {
    axios.post('/accounts/', {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value,
    })
      .then(function (response) {
        // handle success
        console.log(response);

        document.getElementById('alert_box').innerHTML
                 += "<div class='btn btn-primary rounded-pill px-5 mb-3'> 가입을 성공했습니다. </div>"
      })
      .catch(function (error) {
      // handle failure
        console.log(error);

        document.getElementById('alert_box').innerHTML
                 += "<div class='btn btn-danger rounded-pill px-5 mb-3'> 가입을 실패했습니다. </div>"
      });
}