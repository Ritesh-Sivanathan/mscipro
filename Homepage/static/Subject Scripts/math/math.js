window.onload = function() {
    var modal = document.getElementById('myModal');
    var span = document.getElementsByClassName("close")[0];
    var sat = document.getElementById('open-modal');

    sat.addEventListener("click", function() {
        modal.style.display = "block";
    })
    
    
    span.addEventListener("click", function() {
        modal.style.display = "none";
    });
}