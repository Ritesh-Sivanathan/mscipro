window.onload = function() {
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];

    if (localStorage.getItem('modalShown') !== 'true') {
        modal.style.display = "block";
        localStorage.setItem('modalShown', 'true');
    }
    
    span.addEventListener("click", function() {
        modal.style.display = "none";
    });

    mathClick = document.getElementById('math-click')
    scienceClick = document.getElementById('science-click')
    programmingClick = document.getElementById('programming-click')

    mathDropdown = document.getElementById('math-dropdown-content')
    scienceDropdown = document.getElementById('science-dropdown-content')
    programmingDropdown = document.getElementById('programming-dropdown-content')

    mathState = 0
    scienceState = 0
    programmingState = 0

    mathClick.addEventListener('click', function() {
        if (mathState == 0) {
            mathDropdown.style.display = "block";
            mathState = 1
        } else if (mathState == 1) {
            mathDropdown.style.display = "none";
            mathState = 0;
        }
    })

    scienceClick.addEventListener('click', function() {
        if (scienceState == 0) {
            scienceDropdown.style.display = "block";
            scienceState = 1
        } else if (scienceState == 1) {
            scienceDropdown.style.display = "none";
            scienceState = 0;
        }
    })

    programmingClick.addEventListener('click', function() {
        if (programmingState== 0) {
            programmingDropdown.style.display = "block";
            programmingState = 1
        } else if (programmingState == 1) {
            programmingDropdown.style.display = "none";
            programmingState = 0;
        }
    })

}