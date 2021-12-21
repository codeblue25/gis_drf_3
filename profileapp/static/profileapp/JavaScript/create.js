
function send_input() {
    var form = new FormData();
    form.append('nickname', document.getElementById('nickname').value);
    form.append('image', document.getElementById('image').files[0]);
    form.append('message', document.getElementById('message').value);

    axios({
        method: 'post',
        url: '/profiles/',
        data: form,
        headers: {
            Authorization: decodeURIComponent(getCookie('drf_token'))
        }
      })

      .then(function (response) {
        // handle success
        console.log(response);

        // redirect success_url
        window.location.href = '/accounts/retrieve_template/' + response.data['owner_id'];
      })
      .catch(function (error) {
      // handle failure
        console.log(error);

        document.getElementById('alert_box').innerHTML
                 += "<div class='btn btn-danger rounded-pill px-5 mb-3'> 프로필 생성을 실패했습니다</div>"
      });
}