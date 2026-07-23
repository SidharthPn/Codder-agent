let passwordLength = 12;
let charactersToUse = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+~`|}{[]:;?><,./=-";
let displayArea = document.getElementById("password-display");

function generateRandomCharacter() {
    return charactersToUse.charAt(Math.floor(Math.random() * charactersToUse.length));
}

function generatePassword() {
    let password = "";
    for (let i = 0; i < passwordLength; i++) {
        password += generateRandomCharacter();
    }
    updateDisplay(password);
}

function updateDisplay(password) {
    displayArea.textContent = password;
}

document.getElementById("generate-button").addEventListener("click", generatePassword);

document.addEventListener("DOMContentLoaded", function() {
    // Add event listener to the password length input field
    document.getElementById("password-length").addEventListener("input", function() {
        passwordLength = parseInt(this.value);
    });

    // Add styles to the UI elements
    let passwordDisplay = document.getElementById("password-display");
    passwordDisplay.className = "password-display";
    let generateButton = document.getElementById("generate-button");
    generateButton.className = "generate-button";
    let passwordLengthInput = document.getElementById("password-length");
    passwordLengthInput.className = "password-length-input";
});