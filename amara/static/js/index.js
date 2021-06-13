function execute_ajax() {

    body = {
        name: "Santhohs",
        email: "santhosh.kbr@gmail.com"
    } ;
    axios
    .post("/ajax_form", body)
    .then((response) => {
        console.log(response);
    }, (error) => {
        console.log(error);
    });

    // axios.post("/ajax_form", body, { headers: {
    //     'Content-Type': 'json'
    // }}).then(response => {
    //     console.log("Ajax Successful")
    //     let table_data = document.getElementById("table_data");
    //     for (let i = 0; i < complete_subscriptions.length; i++) {
    //         let row = document.createElement("TR");
    //         row.className = "item";
    //         let name = document.createElement("TD");
    //         let email = document.createElement("TD");
    //         let subscriptions = document.createElement("TD");
    //         name.appendChild(document.createTextNode(complete_subscriptions[i].fields.name));
    //         email.appendChild(document.createTextNode(complete_subscriptions[i].fields.email));
    //         subscriptions.appendChild(document.createTextNode(complete_subscriptions[i].fields.subscriptions));
    //         row.appendChild(name);
    //         row.appendChild(email);
    //         row.appendChild(subscriptions);
    //         table_data.appendChild(row);
    //     }
    // }).catch(function(error) {
    //     console.log("Ajax failed");
    //     console.log(error);
    // });
}