var elements = document.getElementsByClassName("item");
for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', myFunction, false);
}
async function myFunction() {
    name = this.childNodes[0].title;
    chrome.runtime.sendMessage({
        name: name
    });
}

