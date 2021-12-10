<!--  서버 호출 함수  -->
function send_input() {
    axios.post('/accounts/hello_world/', {
        input_data: document.getElementById('input_data').value,
      })
      .then(function (response) {
        // handle success
        console.log(response);
        // POST 요청이 성공했을 때 하는 JS 작업: Hello JS!
        document.getElementById('text').innerHTML = response.data['message'];

      })
      .catch(function (error) {
        console.log(error);
      });
}