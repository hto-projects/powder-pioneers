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
    name: "nuke",
    price: 0.99,
    image:"images/nuke.jpg",
    quantity: 0
  }
]


function openForm(){
  document.querySelector(".content").style.display = "none";
  document.querySelector(".form").style.display = "block";
}

var cartButton = document.querySelector("#cart-button");
//cartButton.addEventListener("click", openForm);


function enter(){
  let longitude = document.querySelector("#log").value;
  let latitude = document.querySelector("#lat").value;
  //41.4623485,-81.9280317
  let lonLatString = latitude+","+longitude;
  let requestString = "http://127.0.0.1:8080/"+lonLatString+","+window.location.href
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