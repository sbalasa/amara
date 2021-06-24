const form = document.getElementById('ajax_form');
const tbody = document.querySelector('tbody')
console.log(tbody)

const csrf = document.getElementsByName('csrfmiddlewaretoken')

const name = document.getElementById('id_name');
const email = document.getElementById('id_email');
const subscription = document.getElementById('id_subscription');

const url = '';

form.addEventListener('submit', (e)=>{
    e.preventDefault();
    fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value);
    fd.append('name',  name.value);
    fd.append('email',  email.value);
    fd.append('subscription',  subscription.value);

    $.ajax({
        type: 'POST',
        url: url,
        data: fd,
        success: function(response){
            tbody.innerHTML += `<tr>
                <td>${name.value}</td>
                <td>${email.value}</td>
                <td>${subscription.value}</td>
            </tr>`
            console.log(name.value)
            console.log(response)
            name.value=''
            email.value=''
            subscription.value=''
        },
        error: function(error){
                console.log(error)
            },
        cache: false,
        contentType: false,
        processData: false
    })
})

