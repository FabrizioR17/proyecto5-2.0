const htmlList = document.querySelector('#html_list')

const localToken = JSON.parse(localStorage.getItem('localToken')) ?? window.location.replace('./login.html')


async function getPagos() {
  try {
    
    const options = {
      method:'GET',
      headers: {
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + localToken.access
      }
    }
    const response = await fetch('http://127.0.0.1:8000/payment/', options)
    const data = await response.json()

    console.log(data)

    data.results.forEach((registro) => {
      htmlList.innerHTML += listaPagos(registro)
    });

  } catch (error) {
    console.log(error)
  }
}

function listaPagos(value) {
  return `
  <li>Monto: <strong>${value.amount}</strong></li>
  <li>Expiracion: ${value.expiration_date}</li>
  <li>Dia del pago: ${value.payment_date}</li>
  <li>ID de pago: ${value.id}</li>
  <li>ID del servicio: ${value.service_id}</li>
  <li>ID del usuario: ${value.user_id}</li>
  <hr></hr>
  `
}

getPagos()
