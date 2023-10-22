document.addEventListener('DOMContentLoaded', function () {
    var links = document.querySelectorAll('button[data-target]'); // Change 'button' to the appropriate element type, e.g., 'a' if using anchor tags.
  
    links.forEach(function (link) {
      link.addEventListener('click', function (event) {
        event.preventDefault();
        var targetId = link.getAttribute('data-target');
        var targetElement = document.getElementById(targetId);
        if (targetElement) {
          targetElement.scrollIntoView({
            behavior: 'smooth',
          });
        }
      });
    });
  });