// get execuuted as soon as the chrome extension is either installed/refreshed, no delay happened 
// console.log("from background"); 

// add a listener to see which tabs users are at / what users are doing 
let active_tab_id = 0; 

// $(document).ready(jQueryMain);

chrome.tabs.onActivated.addListener(tab => {
    chrome.tabs.get(tab.tabId, current_tab_info => {
        // console.log(current_tab_info.url); 
        active_tab_id = tab.tabId; 

        // if it's on https://www.google, inject the script 
        if (/^https:\/\/www\.amazon/.test(current_tab_info.url)) {
            chrome.tabs.insertCSS(null, {file: './mystyles.css'}); 
            chrome.tabs.executeScript(null, {file: './foreground.js'}, () =>  console.log("I injected")); 

            // chrome.tabs.executeScript(null, {file: './popup.js'}, () =>  console.log("Popup script executed")); 
        }
    }) 
});


chrome.storage.local.get("subtotal", value => {
    if (value) {
        console.log(value); 
    } else {
        console.log("No Price"); 
    }
}); 

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    // if (request.message === 'yo check the storage') {

    //     chrome.tabs.sendMessage(active_tab_id, {message: 'yo i got your message'}); 

        chrome.storage.local.get("subtotal", value => {
            console.log(value); 
        }); 
    // }
}); 
