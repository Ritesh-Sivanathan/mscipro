window.onload = function() {
    var modal = document.getElementById('myModal');
    var span = document.getElementsByClassName("close")[0];

    if (localStorage.getItem('modalShown') !== 'true') {
        modal.style.display = "block";
        localStorage.setItem('modalShown', 'true');
    }

    span.addEventListener("click", function() {
        modal.style.display = "none";
    });
}