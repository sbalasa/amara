function execute_ajax() {
    let body = JSON.stringify({
        name: document.querySelector("#name").value,
        email: document.querySelector("#email").value,
        subscriptions: document.querySelector("#input_subscriptions").value
    })
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "XCSRF-TOKEN";
    axios
        .post("/ajax_form", body)
        .then((response) => {
            let complete_subscriptions = response.data;
            let table_data = document.getElementById("table_data");
            for (let i = 0; i < complete_subscriptions.length; i++) {
                let row = document.createElement("TR");
                row.className = "item";
                let name = document.createElement("TD");
                let email = document.createElement("TD");
                let subscriptions = document.createElement("TD");
                name.appendChild(document.createTextNode(complete_subscriptions[i].fields.name));
                email.appendChild(document.createTextNode(complete_subscriptions[i].fields.email));
                subscriptions.appendChild(document.createTextNode(complete_subscriptions[i].fields.subscriptions));
                row.appendChild(name);
                row.appendChild(email);
                row.appendChild(subscriptions);
                table_data.appendChild(row);
            }
        }, (error) => {
            console.log(error);
        });
}