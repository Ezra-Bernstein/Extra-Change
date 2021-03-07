chrome.storage.local.get("subtotal", value => {
    if (value) {
        var totalPrice = value["subtotal"]; 
        var donatePrice = getExtraChange(totalPrice); 

        console.log("hello: " + value["subtotal"]); 

        $('#totalPrice').html('$' + totalPrice); 
        $('#donatePrice').html('$' + donatePrice)
        // $('#amnt').value(donatePrice); 

        $('#formID').append('<input type="hidden" name="amount" id="amnt"' + 'value="' + donatePrice + '"></input>'); 
        // <input type="hidden" name="amount" id="amnt" value="0.0"></input>

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


$.get("https://extra-change.ue.r.appspot.com/getFundList", function(data, status) {
    // console.log("received"); 

    // var parse_data = JSON.parse(data); 

    // var dataString = JSON.stringify(data); 

    var dataObjArray = data["data"]; 

    for (var i = 0; i < dataObjArray.length; i++) {
        var name = dataObjArray[i]["name"];
        var creator = dataObjArray[i]["creator"];

        var valueElemnt = name + ',' + creator; 

        $('#myList').append('<option value ="' + valueElemnt + '">' + name + '</option>'); 
    }


    // alert(dataObjArray[0]["name"]); 

    // $('#test').html(parse_data[0]); 
})
