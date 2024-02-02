// script for arithmetic/problem gen

document.addEventListener("DOMContentLoaded", function () {

    // get all buttons and fields that need to be dynamically changed
    // include difficulty display, score display, generate problem btn, problem space, answer query, check answer button, difficult selection button

    const generateBtn = document.getElementById("generateBtn");
    const problemText = document.getElementById("problem");
    const userAnswer = document.getElementById("userAnswer");
    const checkBtn = document.getElementById("checkBtn");
    const resultText = document.getElementById("result");
    const digitSelect = document.getElementById("digit-select");
    const scoreElement = document.getElementById("score");
    const skippedText = document.getElementById("skipped");
    const highScore = document.getElementById('high-score');

    // score is set to 0 as default. will be replaced with stored info later

    var score = 0;
    var hscore = 0;

    function oldHighScore() {
        highScore.textContent = ` High Score: ${getHighScore()}`;
    }

    oldHighScore() // initial score setting to update html

    function newHighScore() { // used when user gets answr correct
        if (score > localStorage.getItem('hscore')) {
            localStorage.setItem('hscore', score);
        }
    }

    function getHighScore() {
        if (localStorage.getItem('hscore') == null) {
            localStorage.setItem('hscore', 0);
        } 

        return localStorage.getItem('hscore')
    }

    getHighScore()
    
    // find the difficulty selected by user

    function getSelectedOption() {
        const selectedValue = digitSelect.value;
        var maxRange;
        
        switch (selectedValue) {
            case "single-digit":
                maxRange = 10;
                updateDifficulty("Single Digit");
                break
            case "double-digit":
                maxRange = 99;
                updateDifficulty("Double Digit");
                break
            case "triple-digit":
                maxRange = 999;
                updateDifficulty("Triple Digit")
            case "quadruple-digit":
                maxRange = 9999;
                updateDifficulty("Quadruple Digit");
        }

        // using max range corresponding to the selected difficulty level with the generate problem function

        generateProblem(maxRange);
    }

    // update difficulty after start

    function updateDifficulty(difficulty) {
        const headerElement = document.getElementById("difficulty");
        headerElement.textContent = `Selected Difficulty: ${difficulty}`;
    }

    // problem generation function

    function generateProblem(maxRange) {
        
        const num1 = Math.floor(Math.random() * (maxRange + 1));
        const num2 = Math.floor(Math.random() * (maxRange + 1));
        const problem = `${num1} + ${num2} = ?`;
        problemText.textContent = problem;
    }

    generateBtn.addEventListener("click", getSelectedOption);


    // event listener for check answer btn

    checkBtn.addEventListener("click", function () {
        const userProvidedAnswer = parseInt(userAnswer.value, 10);
        const problemParts = problemText.textContent.split(" ");
        const correctAnswer = parseInt(problemParts[0]) + parseInt(problemParts[2]);

        if (userProvidedAnswer === correctAnswer) {
            resultText.textContent = "Correct!";
            score++;

            // correct answer -> prob gen
            getSelectedOption();
        } else {
            resultText.textContent = "Incorrect. Try again.";
        }

        // update  score
        scoreElement.textContent = `Score: ${score}`;
        newHighScore()
        oldHighScore()
    });
});
