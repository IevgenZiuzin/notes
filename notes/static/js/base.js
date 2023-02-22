window.onload = () =>{
    let delete_buttons = document.querySelectorAll('.delete')
    delete_buttons.forEach( button =>{
        button.addEventListener('click', async evt => {
            evt.preventDefault()
            data = {
                id: +button.getAttribute('note_id')
            }
            parent = button.closest('.notecard')
            await fetch("/mynotes/api/delete/", {
                method: 'DELETE',
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                body: JSON.stringify(data)
            })
                .then(response => {
                    if (response.ok) {
                        parent.remove()
                    }
                })
                .catch(data => console.log(response.statusText, `\nstatus: ${response.status}`))
        })
    })
        let search_input = document.querySelector('[name=search_match]')
        search_input.addEventListener('input', async evt => {
            searchForm = search_input.closest('form')
            data = {
                search_match: searchForm.querySelector('[name=search_match]').value,
                date_from: searchForm.querySelector('[name=date_from]').value,
                date_to: searchForm.querySelector('[name=date_to]').value
            }
            await fetch("/mynotes/api/search/", {
                method: 'POST',
                headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken")},
                body: JSON.stringify(data)
            })
            .then(response => {
                if(response.ok){
                    return response.text()
                }
                else{
                    console.log(response.statusText, `\nstatus: ${response.status}`)
                }
            })
            .then(data => {
                document.querySelector('.search-results').innerHTML = data
            })
    })
}
window.onclick = function(e){
    document.querySelector('.search-results').innerHTML = ''
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