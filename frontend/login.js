const html_forms = document.querySelector("#htmlLogin");
const inputs = document.querySelectorAll("input");




html_forms.onsubmit = async function (event) {
  event.preventDefault()

  const body = {}

  inputs.forEach((input) => {
    body[input.name] = input.value
  });

  const body_json = JSON.stringify(body);

  try {
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: body_json,
    };
    const response = await fetch('http://127.0.0.1:8000/token/', options);
    const data = await response.json();


    console.log(data)


    if (data.detail) {
      console.log('error')


    } else {
      const responseID = await fetch(`http://127.0.0.1:8000/get-usuarios/${body.username}/`);
      const dataID = await responseID.json();


      localStorage.setItem('localID', JSON.stringify(dataID))
      localStorage.setItem('localToken', JSON.stringify(data))
      // window.location.replace('/js_project/main/html/payments.html')
    }
  } catch (error) {
    console.log(error)
  }
}