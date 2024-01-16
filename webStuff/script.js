
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
  },
  {
    name:"nuke" ,
    price:0.990,
    image:"images/nuke.jpg",
    quantity:0
  },
  {
    name:"Nerds Box" ,
    price:2.00,
    image:"images/Nerds.png",
    quantity:0
  },
  {
    name:"Playstation" ,
    price:100.00,
    image:"images/Playstation.png",
    quantity:0
  },
  {
    name:"The Grippers" ,
    price:100.00,
    image:"images/theConcreteGrippers.jpg",
    quantity:0
  },
  {
    name:"Binary Watch" ,
    price:300.00,
    image:"images/Watch.jpeg",
    quantity:0
  }
]

window.onload = function() {
  document.querySelector("#banner-header").style.opacity = "1";
  document.querySelector("#banner-text").style.opacity = "1";
  document.querySelector("#banner-btn").style.opacity = "1"
}

function openForm(){
  document.querySelector(".banner").style.display= "none";
document.querySelector(".content").style.display = "none";
  document.querySelector(".form").style.display = "block";

  document.querySelector("#aboutBtn").style.display = "inline";
  spliceCart();
  cartString();
  
  console.log(cartNameString);
  displayCart();
}

function closeForm(){
  document.querySelector(".content").style.display = "block";
  document.querySelector(".form").style.display = "none";

  document.querySelector(".banner").style.display= "none";

  document.querySelector("html").style.backgroundColor = "#f0f0f0";
  document.querySelector("#nav-bar").style.display = "block";
}


var toggle = true;

function toggleFunction(){
    toggle ? A() : B();
    toggle = !toggle;
}

function A() {
  document.querySelector("#sidebar").style.display = "block";
}

function B() {
  document.querySelector("#sidebar").style.display = "none";
}

var cartButton = document.querySelector("#cart-button");
//cartButton.addEventListener("click", openForm);


function enter(){
  let longitude = document.querySelector("#log").value;
  let latitude = document.querySelector("#lat").value;
//return if either return null
  if (latitude == "" || latitude == 0 || longitude == "" || longitude == 0) 
  {
    alert("please add latitude and longitude of drone delivery location");
  }
  
  


  //41.4623485,-81.9280317
  let lonLatString = latitude+","+longitude;
  let requestString = "http://127.0.0.1:8080/"+lonLatString+","+cartNameString+","+window.location.href
  
  //window.location.replace(requestString);
  
  
  //window.open(requestString).focus();
  alert(requestString+" if you are seeing this on the replit, the submit button works, bad news is the redirect does not work on replit. this is expected behavior and will work for the demo, also please notify me of any changes that you make so that I can add them to the github repo"); //this is apparently REQUIRED for the website to talk to the drone
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
 
}

var newCart = []
var tempCart = []

function spliceCart() {
  for (let i=0; i<cart.length; i++){

    let tempItem = cart[i]
    
    if(newCart.indexOf(tempItem) < 0){
      newCart.push(tempItem);
    }
  }
}

let cartNameString = ""
  function cartString(){ 
    for (let i=0; i<newCart.length; i++){
      let tempItem = newCart[i];
      let tempItemString = tempItem.name+","+tempItem.quantity;

      tempCart.push(tempItemString);
    }
    console.log(tempCart)
   cartNameString = JSON.stringify(tempCart);
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
    qtyMinusBtn.class = "qty-minus"
    qtyMinusBtn.id = itemNameElement.textContent;
    qtyMinusBtn.setAttribute("onClick", `minusQty(${i})`);

    
  
    
    qtyPlusBtn.textContent = "+"
    qtyPlusBtn.id = "qty-plus"
    qtyPlusBtn.setAttribute("onClick", `plusQty(${i})`);
    
      itemQtyElement.textContent = newCart[i].quantity;
      itemQtyElement.id = "cart-item-qty";
      itemQtyElement.class = "cart-item"
      rowElement.appendChild(qtyMinusBtn);
      rowElement.appendChild(itemQtyElement);
      rowElement.appendChild(qtyPlusBtn);
  }

  let totalElement = document.getElementById("total");
  //console.log("Total Element Get by id")
  //console.log(totalElement);


  console.log(total);
  totalElement.textContent = "Your total is: " +"$"+total.toFixed(2);
  //totalElement.textContent = "Your total is: " +"$"+ total; 
}

function minusQty(index){
  if (newCart[index].quantity > 0) 
    {
      newCart[index].quantity --
      total = total - newCart[index].price;
      //total = Math.round((total - newCart[index].price) * (10 ** 2)) / (10 ** 2)
       displayCart()
    }
  else {
    return;
  }
}

function plusQty(index){
  newCart[index].quantity ++
  total = (total + newCart[index].price);
  //total = Math.round((total + newCart[index].price) * (10 ** 2)) / (10 ** 2)
   displayCart();
}