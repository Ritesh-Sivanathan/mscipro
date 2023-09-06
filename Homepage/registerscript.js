document.addEventListener("DOMContentLoaded", function () {
    const registerButton = document.getElementById("register-button");

    registerButton.addEventListener("click", function () {

        const emailInput = document.querySelector('input[type="email"]').value;
        const passwordInput = document.querySelector('input[type="password"]').value;


        if (emailInput && passwordInput) {

            window.location.href = "homepage.html";
        } else {
            alert("Please fill in both email and password fields.");
        }
    });
});