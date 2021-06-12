function execute_ajax() {
    let ajax_response = false;
    var token = document.getElementsByName("csrfToken").value;
    $.ajax({
        type: "POST",
        url: "/ajax_form",
        contentType: 'application/json',
        headers: {
            'X-CSRF-Token': token 
        },
        data: JSON.stringify({
            name: document.querySelector("#name").value,
            email: document.querySelector("#email").value,
            subscriptions: document.querySelector("#input_subscriptions").value
        }),
        success: function(res) {
            let complete_subscriptions = JSON.parse("{{ complete_subscriptions | escap_js }}");
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
            ajax_response = true;
        },
        error: function() {
            console.log("Ajax Failed");
        },
        async: false
    });
    return ajax_response;
}