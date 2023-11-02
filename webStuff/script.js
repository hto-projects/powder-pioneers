
var items = [
  {
    name: "Shoe",
    price: 5.00,
    image:"images/shoe.jpg",
    quantity: 0
  },
  {
    name: "Realistic Sword",
    price: 50.00,
    image:"images/sword.jpg",
    quantity: 0
  },
  {
    name: "Modern House",
    price: 100.00,
    image: "images/house.jpg",
    quantity: 0
  },
  {
    name: "Basilisk",
    price: 5.00,
    image:"images/basilisk.png",
    quantity: 0
  }
]


function openForm(){
  document.querySelector(".content").style.display = "none";
  document.querySelector(".form").style.display = "block";
  spliceCart();
  displayCart();
}

var cartButton = document.querySelector("#cart-button");
//cartButton.addEventListener("click", openForm);


function enter(){
  let longitude = document.querySelector("#log").value;
  let latitude = document.querySelector("#lat").value;
  //41.4623485,-81.9280317

  let cartString = JSON.stringify(cart[0].name);
  //41.4623485,-81.9280317
  let lonLatString = latitude+","+longitude;
  let requestString = "http://127.0.0.1:8080/"+lonLatString+","+window.location.href+","+cartString

  //let lonLatString = latitude+","+longitude;
  //let requestString = "http://127.0.0.1:8080/"+lonLatString+","+window.location.href
  window.location.replace(requestString);
  alert(requestString); //this is apparently REQUIRED for the website to talk to the drone
  //fetch(requestString,{mode: 'cors'});
  //fetch("http://127.0.0.1:8080/41.4623485,-81.9280317")

  //*click* that was easy
  //tell me on discord when you are ready for me to test this with the drone
}

var cart = []
var total = 0

function addToCart(itemIndex) {
  let item = items[itemIndex];
  cart.push(item);
  item.quantity++;
  total = total + item.price;

  console.log(cart);
  console.log(total);
}

var newCart = []

function spliceCart() {
  for (let i=0; i<cart.length; i++){

    let tempItem = cart[i]
    
    if(newCart.indexOf(tempItem) < 0){
      newCart.push(tempItem);
    }
  }
}

function displayCart() {
  let tableElement = document.querySelector("#cart-display");
  tableElement.innerHTML = "";

  // Creates header row
  let rowElement = document.createElement("tr")
  tableElement.appendChild(rowElement);

  let nameLabel = document.createElement("th");
  let priceLabel = document.createElement("th");
  let qtyLabel = document.createElement("th");
  let gap = document.createElement("th")

  gap.textContent = ""
  nameLabel.textContent = "Item"
  nameLabel.id = "name-label"
  priceLabel.textContent = "Price"
  priceLabel.id = "price-label"
  qtyLabel.textContent = "Qty"
  qtyLabel.id = "qty-label"

  rowElement.appendChild(gap)
  rowElement.appendChild(nameLabel)
  rowElement.appendChild(priceLabel)
  rowElement.appendChild(qtyLabel)
  
  for(let i=0; i<newCart.length; i++) {
    //create a row
    let rowElement = document.createElement("tr")
    tableElement.appendChild(rowElement);


    //creates table cell w the image
      let imgElement = document.createElement("img");
      imgElement.src = newCart[i].image;
      imgElement.id = "cart-image";
      rowElement.appendChild(imgElement)

    //creates table cell w the name
      let itemNameElement = document.createElement("td");
      itemNameElement.textContent = newCart[i].name;
      itemNameElement.id = "cart-item-name";
      itemNameElement.class = "cart-item"
      rowElement.appendChild(itemNameElement)

    //creates table cell w the price
      let itemPriceElement = document.createElement("td");
      itemPriceElement.textContent = newCart[i].price.toFixed(2);
      itemPriceElement.id = "cart-item-price";
      itemPriceElement.class = "cart-item"
      rowElement.appendChild(itemPriceElement);

    //creates table cell w the quantity
      let itemQtyElement = document.createElement("td");
      let qtyMinusBtn = document.createElement("button")
      let qtyPlusBtn = document.createElement("button")

    qtyMinusBtn.textContent = "-"
    qtyMinusBtn.id = "qty-minus"
    qtyMinusBtn.onClick = "minusQty("+itemNameElement+")"
    qtyPlusBtn.textContent = "+"
    qtyPlusBtn.id = "qty-plus"
    qtyPlusBtn.onClick = "plusQty("+itemNameElement+")"
    
      itemQtyElement.textContent = newCart[i].quantity;
      itemQtyElement.id = "cart-item-qty";
      itemQtyElement.class = "cart-item"
      rowElement.appendChild(qtyMinusBtn);
      rowElement.appendChild(itemQtyElement);
      rowElement.appendChild(qtyPlusBtn);
   
  }
  
}

function minusQty(itemNameElement){
  let x = newCart.indexOf(itemNameElement);
  cart[x].quantity --
  displayCart()
}

function plusQty(){
  let x = newCart.indexOf(itemNameElement);
  cart[x].quantity ++
  displayCart()
}