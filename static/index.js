function scrollToSection(sectionId) {
  let section = document.getElementById(sectionId);
  if (section) {
    section.scrollIntoView({ behavior: "smooth" });
  }
}

/** Adding "active" to activated navbar links including the searchbar */
const activePath = window.location.pathname;
const navLinks = document.querySelectorAll(".nav-link").forEach((link) => {
  if (link.getAttribute("href") === activePath) {
    link.classList.add("active");
  }
});

function activateSearchbar(isActive) {
  if (isActive) {
    console.log("activating search bar");
    document.querySelector(".searchbar").classList.add("active");
  } else {
    console.log("deactivating search bar");
    document.querySelector(".searchbar").classList.remove("active");
  }
}

/** Handle the clear search bar button */
function clearSearchBar() {
  let input = document.querySelector(".searchbar-input");
  input.value = "";
}

/** Make cards look like Pinterest by assigning them a random card size */
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

/** Creating the Sundays drop down for the meal planner form */
// Getting a list of Sundays
function getSundays() {
  let sundays = [];
  let currentSunday = new Date();

  // Set to the current week's Sunday
  currentSunday.setDate(
    currentSunday.getDate() - ((currentSunday.getDay() + 7) % 7)
  );
  // console.log("Current Sunday:", currentSunday);

  // Generate next 5 Sundays
  for (let i = 0; i < 5; i++) {
    sundays.push(new Date(currentSunday));
    currentSunday.setDate(currentSunday.getDate() + 7);
  }
  // console.log(sundays);

  return sundays;
}

// Populating the list of Sundays in a dropdown
function populateSundaysDropdown() {
  const sundays = getSundays();
  const sundaysDropdown = document.getElementById("week_start");

  if (!sundaysDropdown) {
    console.error("Dropdown element with ID 'week_start' not found");
    return;
  }

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
    sundaysDropdown.appendChild(option);
  });
}

/** Validating that everything in the meal planner form was filled out */
function validateMealPlannerForm(meal) {
  let weekStart = document.getElementById("week_start").value;
  let day = document.getElementById("day").value;

  // Check if both inputs have values
  if (weekStart && day && meal) {
    document.getElementById("submitButton").disabled = false; // Enable submit button
  } else {
    document.getElementById("submitButton").disabled = true; // Disable submit button
  }
}

document.addEventListener("DOMContentLoaded", () => {
  if (window.location.pathname === "/meal-planner-form") {
    // Disable the add button
    document.getElementById("submitButton").disabled = true;
    // Get the sundays dropdown
    populateSundaysDropdown();
    let meal;
    let radioButtons = document.querySelectorAll(".form-check-input");
    radioButtons.forEach((button) => {
      button.addEventListener("change", function () {
        if (this.checked) {
          meal = button.value;
        }
      });
    });
    document.addEventListener("change", (event) => {
      validateMealPlannerForm(meal);
    });
  }
  if (window.location.pathname === "/meal-planner") {
    // Get the sundays dropdown
    populateSundaysDropdown();
  }
});

// handling the click event to delete a recipe
function deleteRecipe(id) {
  let weekStart = document.getElementById("week_start").value.split(" ");
  console.log("deleting:", id);
  console.log("week:", weekStart);
  fetch("/delete", {
    method: "DELETE",
    body: JSON.stringify({ id: id }),
  }).then((_res) => {
    window.location.href = `/meal-planner?week_start=${weekStart[0]}+${weekStart[1]}+${weekStart[2]}+${weekStart[3]}`;
  });
}
