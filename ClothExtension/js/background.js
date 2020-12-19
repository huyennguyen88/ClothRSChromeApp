chrome.runtime.onMessage.addListener(
    function (request) {
        var name = request.name;
        var link = request.link;
        processing(name);
        if(link!=null) processLink(link);
});

async function processing(name) {
    localStorage.setItem("item_name", JSON.stringify(name));
    var imageData = await postData('http://127.0.0.1:5000/predict', { item_name: name })
    localStorage.setItem("items_rs", JSON.stringify(imageData));

}
async function postData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify(data), // string or object
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const myJson = await response.json(); //extract JSON from the http response
    return myJson;
}
function processLink(link){
    chrome.tabs.update({url:link})
}
