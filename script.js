// Add event listener to the nav links
document.querySelectorAll('nav a').forEach((link) => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const href = link.getAttribute('href');
        // Load the corresponding page
        loadPage(href);
    });
});

// Function to load the corresponding page
function loadPage(href) {
    // Use the Fetch API to load the page
    fetch(href)
        .then((response) => response.text())
        .then((html) => {
            // Replace the main content with the loaded page
            document.querySelector('main').innerHTML = html;
        })
        .catch((error) => console.error('Error loading page:', error));
}
