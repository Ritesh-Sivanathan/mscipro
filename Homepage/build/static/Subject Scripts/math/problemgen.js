document.addEventListener("DOMContentLoaded", function () {
    const generateBtn = document.getElementById("generateBtn");
    const problemText = document.getElementById("problem");
    const userAnswer = document.getElementById("userAnswer");
    const checkBtn = document.getElementById("checkBtn");
    const resultText = document.getElementById("result");
    const digitSelect = document.getElementById("digit-select");
    const scoreElement = document.getElementById("score");
    const skippedText = document.getElementById("skipped");
    let score = 0;

    function getSelectedOption() {
        const selectedValue = digitSelect.value;
        let maxRange;
        
        if (selectedValue === "single-digit") {
            maxRange = 10;
            updateDifficulty("Single Digit");
        } else if (selectedValue === "double-digit") {
            maxRange = 99;
            updateDifficulty("Double Digit");
        } else if (selectedValue === "triple-digit") {
            maxRange = 999;
            updateDifficulty("Triple Digit");
        } else if (selectedValue === "quadruple-digit") {
            maxRange = 9999;
            updateDifficulty("Quadruple Digit");
        }

        generateProblem(maxRange);
    }

    function updateDifficulty(difficulty) {
        const headerElement = document.getElementById("difficulty");
        headerElement.textContent = `Selected Difficulty: ${difficulty}`;
    }

    function generateProblem(maxRange) {
        
        const num1 = Math.floor(Math.random() * (maxRange + 1));
        const num2 = Math.floor(Math.random() * (maxRange + 1));
        const problem = `${num1} + ${num2} = ?`;
        problemText.textContent = problem;
    }

    generateBtn.addEventListener("click", getSelectedOption);

    checkBtn.addEventListener("click", function () {
        const userProvidedAnswer = parseInt(userAnswer.value, 10);
        const problemParts = problemText.textContent.split(" ");
        const correctAnswer = parseInt(problemParts[0]) + parseInt(problemParts[2]);

        if (userProvidedAnswer === correctAnswer) {
            resultText.textContent = "Correct!";
            score++;

            // Generate a new problem after a correct answer
            getSelectedOption();
        } else {
            resultText.textContent = "Incorrect. Try again.";
        }

        // Update the score
        scoreElement.textContent = `Score: ${score}`;
    });
});
