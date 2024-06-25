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

/******* Cards *******/
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

/******* Sunday *******/
// Getting a list of Sundays
function getSundays() {
  let sundays = [];
  let currentDate = new Date();

  console.log("Today's date:", currentDate);

  // Set to the current week's Sunday
  currentDate.setDate(currentDate.getDate() - ((currentDate.getDay() + 7) % 7));
  console.log("This Sunday:", currentDate);

  // Generate next 5 Sundays
  for (let i = 0; i < 5; i++) {
    sundays.push(new Date(currentDate));
    currentDate.setDate(currentDate.getDate() + 7);
  }

  return sundays;
}

// Populating the list of Sundays in a dropdown
function populateSundaysDropdown(weekStart) {
  const sundays = getSundays();
  const sundaysDropdown = document.getElementById("week_start");

  // Create a new <option> element that is a placeholder
  const disabledOption = document.createElement("option");
  disabledOption.value = "";
  disabledOption.textContent =
    "Select a starting day for your weekly meal planner";
  disabledOption.disabled = true;
  disabledOption.selected = true;
  sundaysDropdown.append(disabledOption);

  // Populate dropdown with Sundays
  sundays.forEach((sunday) => {
    const option = document.createElement("option");
    option.value = sunday.toDateString();
    option.textContent = sunday.toDateString();

    // Set selected attribute if this option matches week_start
    if (sunday.toDateString() === weekStart) {
      option.selected = true;
    }

    sundaysDropdown.appendChild(option);
  });
}

document.addEventListener("DOMContentLoaded", function () {
  // Get the selected week_start value from the URL
  const urlParams = new URLSearchParams(window.location.search);
  const weekStart = urlParams.get("week_start");

  populateSundaysDropdown(weekStart);

  // Function to check if all required inputs are filled
  function validateForm() {
    var weekStart = document.getElementById("week_start").value;
    var day = document.getElementById("day").value;
    var meal = document.querySelector('input[name="meal"]:checked');

    // Check if both inputs have values
    if (weekStart && day && meal) {
      document.getElementById("submitButton").disabled = false; // Enable submit button
    } else {
      document.getElementById("submitButton").disabled = true; // Disable submit button
    }
  }

  // Initially disable the submit button
  document.getElementById("submitButton").disabled = true;

  // Trigger validation on change of inputs
  document
    .getElementById("week_start")
    .addEventListener("change", validateForm);
  document.getElementById("day").addEventListener("change", validateForm);

  var mealRadios = document.querySelectorAll('input[name="meal"]');
  mealRadios.forEach(function (radio) {
    radio.addEventListener("change", validateForm);
  });
});
