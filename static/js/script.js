// ---------------------------------------------------------------------------
// Client-side validation. This is a first line of defense for user experience
// only -- the Flask backend always re-validates everything server-side.
// ---------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", () => {
    const signupForm = document.getElementById("signup-form");
    const loginForm = document.getElementById("login-form");

    if (signupForm) {
        const password = document.getElementById("password");
        const confirmPassword = document.getElementById("confirm_password");
        const hint = document.getElementById("password-hint");
        

        function validatePasswords() {
            if (confirmPassword.value.length === 0) {
                hint.textContent = "Use 8+ characters.";
                hint.classList.remove("error");
                return true;
            }
            if (password.value !== confirmPassword.value) {
                hint.textContent = "Passwords do not match.";
                hint.classList.add("error");
                return false;
            }
            hint.textContent = "Passwords match.";
            hint.classList.remove("error");
            return true;
        }

        password.addEventListener("input", validatePasswords);
        confirmPassword.addEventListener("input", validatePasswords);

        signupForm.addEventListener("submit", (e) => {
            if (password.value.length < 8) {
                e.preventDefault();
                hint.textContent = "Password must be at least 8 characters.";
                hint.classList.add("error");
                return;
            }
            if (!validatePasswords()) {
                e.preventDefault();
            }
        });
    }

    if (loginForm) {
        loginForm.addEventListener("submit", (e) => {
            const email = document.getElementById("email");
            const password = document.getElementById("password");
            if (!email.value.trim() || !password.value.trim()) {
                e.preventDefault();
                alert("Please fill in both fields.");
            }
        });
    }
});
