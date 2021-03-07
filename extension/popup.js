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

