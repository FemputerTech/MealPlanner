var currentPath = window.location.pathname;

// Find the <a> element with matching href and add 'active' class
document.querySelectorAll('.navbar-nav .nav-link').forEach(function(link) {
    if (link.getAttribute('href') === currentPath) {
        link.classList.add('active');
    }
});