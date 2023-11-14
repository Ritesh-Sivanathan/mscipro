window.onload = function() { // when site is loaded ...

    // selecting respective variables from page
    // including SAT modal, close modal btn, SAT open btn

    var modal = document.getElementById('myModal');
    var span = document.getElementsByClassName("close")[0];
    var sat = document.getElementById('open-modal');

    sat.addEventListener("click", function() { // add event listener for SAT
        modal.style.display = "block";
    })
    
    
    span.addEventListener("click", function() { // add event listener for close btn
        modal.style.display = "none";
    });
}