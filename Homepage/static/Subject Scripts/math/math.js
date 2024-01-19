window.onload = function() {
    
    var modal = document.getElementById('myModal');
    var span = document.getElementsByClassName("close")[0];
    var sat = document.getElementById('open-modal');

    var gradeWork = document.getElementById('ofgrwork');

    var allBoxes = [
        document.getElementById('exams'),
        document.getElementById('ourresources'),
        document.getElementById('rsrcs')
    ];

    sat.addEventListener("click", function() {
        modal.style.display = "block";
    });

    span.addEventListener("click", function() {
        modal.style.display = "none";
    });

    if (localStorage.getItem('mathRUpdate') == null) {
        alert("All resources on this page have been filled as of 1/17/2024. Thank you for your patience. I will be working on a feature to easily manage links so I can fill them out quicker in the future.")
        localStorage.setItem('mathRUpdate', 0)
    }

}


// --- Box focusing animation prototype ---

//     gradeWork.addEventListener('mouseenter', function() {
//         for (var i = 0; i < allBoxes.length; i++) {
//             allBoxes[i].style.animation = "none";
//             void allBoxes[i].offsetWidth; 
//             allBoxes[i].style.animation = "boxHoverFade 0.5s linear";
//             allBoxes[i].style.opacity = 0;
//         }
//     });
    
//     gradeWork.addEventListener('mouseleave', function() {
//         for (var i = 0; i < allBoxes.length; i++) {
//             allBoxes[i].style.animation = "none"; 
//             void allBoxes[i].offsetWidth; 
//             allBoxes[i].style.animation = "boxHoverFadeRelease 0.5s linear";
//             gradeWork.style.animation = "none";
//             allBoxes[i].style.opacity = 1;
//         }
//     });
// }    