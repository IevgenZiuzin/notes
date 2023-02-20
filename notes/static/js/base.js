window.onload = () =>{
    let delete_buttons = document.querySelectorAll('.delete')
    delete_buttons.forEach( button =>{
        button.addEventListener('click', evt => {
            data = {
                id: +button.getAttribute('note_id')
            }
            parent = button.closest('tr')
            request('DELETE', '/', data)
            parent.remove()
        })
    })
    let search_button = document.querySelector('input[name=search]')
    search_button.addEventListener('click', evt =>{
        evt.preventDefault()
        searchForm = search_button.closest('form')
        data = {
            search_match: searchForm.querySelector('[name=search_match]').value,
            date_from: searchForm.querySelector('[name=date_from]').value,
            date_to: searchForm.querySelector('[name=date_to]').value
        }
        request('POST', '/', data)
    })
}

async function request(method, path, data) {
    await fetch(path, {
        method: method,
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify(data)
    })
}



function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}