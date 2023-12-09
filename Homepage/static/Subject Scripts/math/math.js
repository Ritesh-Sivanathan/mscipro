window.onload = function() { // when site is loaded ...

    // selecting respective variables from page
    // including SAT modal, close modal btn, SAT open btn

    var modal = document.getElementById('myModal');
    var span = document.getElementsByClassName("close")[0];
    var sat = document.getElementById('open-modal');
    var usercl = document.documentElement.style.setProperty("--main-background-color", "green");
    var cookies = document.cookies;

    console.log(cookies);

    sat.addEventListener("click", function() { // add event listener for SAT
        modal.style.display = "block";
    })
    
    
    span.addEventListener("click", function() { // add event listener for close btn
        modal.style.display = "none";
    });

    

}