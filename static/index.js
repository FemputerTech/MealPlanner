// Find the <a> element with matching href and add 'active' class
var currentPath = window.location.pathname;
document.querySelectorAll(".navbar-nav .nav-link").forEach(function (link) {
  if (link.getAttribute("href") === currentPath) {
    link.classList.add("active");
  }
});

function activateSearchbar() {
  console.log("activating search bar");
  document.querySelector(".searchbar").classList.add("active");
}

function deactivateSearchbar() {
  console.log("deactivating search bar");
  document.querySelector(".searchbar").classList.remove("active");
}

function clearInput() {
  var input = document.querySelector(".searchbar-input");
  input.value = "";
  input.focus(); // Keep focus on the input after clearing
}

/* Cards */
const cards = document.querySelectorAll(".card-item");
const cardClasses = ["card-small", "card-regular", "card-large"];

// Function to pick a random class from cardClasses array
function getRandomClass() {
  return cardClasses[Math.floor(Math.random() * cardClasses.length)];
}

// Apply random classes to each card-item
cards.forEach((card) => {
  const randomClass = getRandomClass();
  card.classList.add(randomClass);
});
