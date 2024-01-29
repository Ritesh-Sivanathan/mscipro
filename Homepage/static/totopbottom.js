document.addEventListener('DOMContentLoaded', function () {
  var links = document.querySelectorAll('button[data-target]');  

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
