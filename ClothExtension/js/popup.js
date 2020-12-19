var myul = document.getElementsByClassName("list-unstyled")[0]
if (localStorage.getItem("items_rs") !== null) {
  items_rs = JSON.parse(localStorage.getItem("items_rs"))
  ids = items_rs["ids"]
  names = items_rs["names"]
  links = items_rs["links"]
  images = items_rs["images"]
  pricesold = items_rs["pricesold"]
  prices = items_rs["prices"]
  discounts = items_rs["discounts"]
  for (var i = 0; i < ids.length; i++) {
    disStr = ``
    pricesoldStr = ``
    if(discounts[i]!="0%") {
      pricesoldStr = `<span class="priceold text-secondary">${pricesold[i]}</span>`
      disStr = ` <span class="badge badge-danger "> -${discounts[i]}</span>`
    }
    itemHtml = `<li class="item media mt-2 ">
        <a  class="item-link float-left w-25 hvr-grow" href="https://www.zanado.com${links[i]}" title="${names[i]}">
          <img src="https:${images[i]}" class="img-thumbnail rounded">
        </a>       
        <div class="media-body ml-1 container ">
          <div class="row">
            <a class="item-link text-dark col-9 hvr-grow" href="https://www.zanado.com${links[i]}" title="${names[i]}">
              <p >${names[i]}</p>
            </a>
            <div class="col-3">
              ${disStr}
            </div>
          </div>
        <div class="infoprice">
          ${pricesoldStr}
          <span class="pricespecial">${prices[i]}</span>
        </div>

        </div>
      </li>`
    var temp = document.createElement("div")
    temp.innerHTML = itemHtml
    var htmlOj = temp.firstChild
    htmlOj.addEventListener('click', myAction, false)
    myul.appendChild(htmlOj)
  }
}
async function myAction() {
  name = this.childNodes[1].title
  link = this.childNodes[1].href
  chrome.runtime.sendMessage({
    name: name,
    link: link
  });
}