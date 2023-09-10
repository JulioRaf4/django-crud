var prevScrollpos = window.pageYOffset;
var navbar = document.querySelector(".navbar");

window.onscroll = function () {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        // Show the top bar when scrolling up
        navbar.style.top = "30";
    } else {
        // Hide the top bar when scrolling down
        navbar.style.top = "-60px"; // Adjust the height as needed
    }
    prevScrollpos = currentScrollPos;
};
