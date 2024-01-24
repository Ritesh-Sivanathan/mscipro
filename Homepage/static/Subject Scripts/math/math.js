window.onload = function() {
    
    flags = document.getElementsByClassName("flag");

    var flagElements = document.getElementsByClassName("flag");

    function showFlags() {
      if (localStorage.getItem('showFlags') == 1) {
        for (i=0;i<=flagElements.length;i++) {
          document.getElementById(flagElements[i].id).style.display = "inline";
            }
    } else if (localStorage.getItem('showFlags') == 0) {
        for (i=0;i<=flagElements.length;i++) {
          document.getElementById(flagElements[i].id).style.display = "none";
            }
        }
    }

    showFlags()
    
    for (var i=0; i < flagElements.length; i++) {
        if (localStorage.getItem(flagElements[i].id) == 'flagged') {
            document.getElementById(flagElements[i].id).style.backgroundColor = "white";
        }
    }
    
    for (var i=0; i < flagElements.length; i++) {
        flagElements[i].addEventListener("click", flagPressed);
    }

    function assignVals(flag) {
        if (localStorage.getItem(flag) == null) {
            localStorage.setItem(flag, 'not-flagged')
        } 
    }
    
    function flagPressed(event) {
        var clickedFlag = event.currentTarget; // fixes parent/child issue (.target checks the id of the li rather than the button id)
        var flagId = clickedFlag.id;
        assignVals(flagId)
        
        if (localStorage.getItem(flagId) == 'not-flagged') {
                localStorage.setItem(flagId, 'flagged')
                document.getElementById(flagId).style.backgroundColor = "white";
            } else {
                localStorage.setItem(flagId, 'not-flagged')
                document.getElementById(flagId).style.backgroundColor = "grey";
            }
        }

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

}