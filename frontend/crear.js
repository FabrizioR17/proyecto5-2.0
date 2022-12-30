const html_forms = document.querySelector("form");
const inputs = document.querySelectorAll("input");


html_forms.onsubmit = async function (event) {
  event.preventDefault()


  const body = {};

  inputs.forEach((input) => {
    body[input.name] = input.value;
  });

  // console.log(body)

  const body_json = JSON.stringify(body);

  console.log(body_json)


  try {
    const options = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: body_json,
    };

    const response = await fetch("http://127.0.0.1:8000/payment/", options);
    const data = await response.json()

    console.log(response)
    console.log(data)
  
    if (response.ok) {
      console.log("exito");

      Swal.fire({
        icon: "success",
        title: "Guardado...",
      })

    } else {
      console.log("fallo");
    }

  } catch (error) {
    console.log("Algo pasó");
    console.log(error);
  }

}


