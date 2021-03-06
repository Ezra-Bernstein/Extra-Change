// this doesn't get automatically exxcute 
// needs to inject it from background.js
console.log("from foreground"); 
// document.querySelector('#gb').classList.add('spinspinspin'); 

// const first = document.createElement('button'); 
// first.innerText = "SET DATA"; 
// first.id = "first"; 

// const second = document.createElement('button'); 
// second.innerText = "SHOUTOUT TO BACKEND"; 
// second.id = "second"; 

// document.querySelector('body').appendChild(first);
// document.querySelector('body').appendChild(second);

// totalPrice
var totalPriceDollarSign = document.getElementsByClassName("a-size-medium a-color-base sc-price sc-white-space-nowrap")[0].innerText;
var totalPrice = totalPriceDollarSign.substring(1); 
console.log(totalPrice); 
chrome.storage.local.set({"subtotal": totalPrice}); 

// first.addEventListener('click', () => {
    // var totalPrice = totalPriceDollarSign.substring(1); 
    // console.log(totalPrice); 
    // chrome.storage.local.set({"subtotal": totalPrice}); 
// }); 

// second.addEventListener('click', () => {
//     chrome.runtime.sendMessage({message: 'yo check the storage'}); 
//     console.log("I sent the message"); 
// }); 

// chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
//     console.log(request.message); 
// }); 