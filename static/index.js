function scrollToSection(sectionId) {
  let section = document.getElementById(sectionId);
  if (section) {
    section.scrollIntoView({ behavior: "smooth" });
  }
}

/** Adding "active" to activated navbar links */
document.addEventListener("DOMContentLoaded", () => {
  const activePath = window.location.pathname;
  const navLinks = document.querySelectorAll(".nav-link").forEach((link) => {
    if (link.getAttribute("href") === activePath) {
      link.classList.add("active");
    }
  });
});

/** Adding "active" to activated planner days */
document.addEventListener("DOMContentLoaded", () => {
  const activePath = window.location.href.split("=");
  const activeDay = activePath[1];
  document.querySelectorAll(".day-button").forEach((day) => {
    if (day.getAttribute("value") === activeDay) {
      day.classList.add("active");
    }
  });
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
// Function to pick a random class from cardClasses array
function getRandomClass() {
  const cardClasses = ["card-small", "card-regular", "card-large"];
  let randomClass = cardClasses[Math.floor(Math.random() * cardClasses.length)];
  return randomClass;
}

document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card-item");
  // Apply random classes to each card-item
  cards.forEach((card) => {
    const randomClass = getRandomClass();
    card.classList.add(randomClass);
  });
});

// handling the click event to delete a recipe
function deleteRecipe(id, day) {
  console.log("deleting:", id);
  fetch("/meal-planner", {
    method: "DELETE",
    body: JSON.stringify({ id: id }),
  }).then((_res) => {
    window.location.href = `/meal-planner?day=${day}`;
  });
}

/** Validating that everything in the meal planner form was filled out */
function validateMealPlannerForm(meal) {
  let day = document.getElementById("day").value;

  // Check if both inputs have values
  if (day && meal) {
    document.getElementById("submitButton").disabled = false; // Enable submit button
  } else {
    document.getElementById("submitButton").disabled = true; // Disable submit button
  }
}

document.addEventListener("DOMContentLoaded", () => {
  if (window.location.pathname === "/meal-planner-form") {
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
});
