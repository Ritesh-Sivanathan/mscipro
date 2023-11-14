// Script to add function to the "To Top" and "To Bottom" buttons on various pages on MSCIPro's website
// The specified buttons only appear at small resolutions (check individual page stylings for more details)

document.addEventListener('DOMContentLoaded', function () { // check to see if the page is loaded
    var links = document.querySelectorAll('button[data-target]');  // select all instances of the button
  
    links.forEach(function (link) { // iterate through each link
      link.addEventListener('click', function (event) {
        event.preventDefault();
        var targetId = link.getAttribute('data-target'); // get target variables
        var targetElement = document.getElementById(targetId);
        if (targetElement) {
          targetElement.scrollIntoView({ // actual scrolling function
            behavior: 'smooth', // define the scroll movement to smooth
          });
        }
      });
    });
  })


