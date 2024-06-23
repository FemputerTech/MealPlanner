// Find the <a> element with matching href and add 'active' class
var currentPath = window.location.pathname;
document.querySelectorAll('.navbar-nav .nav-link').forEach(function(link) {
    if (link.getAttribute('href') === currentPath) {
        link.classList.add('active');
    }
});

function activateSearchbar() {
    console.log("activating search bar")
    document.querySelector('.searchbar').classList.add('active');
}

function deactivateSearchbar() {
    console.log("deactivating search bar")
    document.querySelector('.searchbar').classList.remove('active');
}

function clearInput() {
    var input = document.querySelector('.searchbar-input');
    input.value = '';
    input.focus(); // Keep focus on the input after clearing
}