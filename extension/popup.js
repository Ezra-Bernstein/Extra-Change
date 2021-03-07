chrome.storage.local.get("subtotal", value => {
    if (value) {
        var totalPrice = value["subtotal"]; 
        var donatePrice = getExtraChange(totalPrice); 

        console.log("hello: " + value["subtotal"]); 

        $('#totalPrice').html('$' + totalPrice); 
        $('#donatePrice').html('$' + donatePrice)
        $('#amnt').value(donatePrice); 

    } else {
        console.log("No Price"); 
    }
}); 


function getExtraChange(subtotal) {
    var priceNum = parseFloat(subtotal); 
    var roundUpPrice = Math.ceil(priceNum); 
    var extraChange = (roundUpPrice - priceNum).toFixed(2); 
    return extraChange; 
}

// let url = 'http://0.0.0.0:5000/getFundList';
//         fetch(url, {
//             method: "GET",
//         }).then((response) => {
//             let json = response.json();
//             console.log(json);
//         }).catch((err) => {
//             console.error(err)
//         });
//example output:
// {<name of fund>: <user that created fund>}
// {'my other fnd': 'user2@gmail.com', 'my other fund': 'user2@gmail.com', 'my fund': 'user@example.com'}