document.addEventListener("DOMContentLoaded", function () {
    // H1 click handler
    const el = document.getElementById("name");
    if (!el) {
        console.error("script.js: element with id 'name' not found");
        return;
    }

    console.log("script.js loaded: attaching click listener to #name");
    el.addEventListener("click", function () {
        console.log("#name clicked");
        this.style.setProperty("color", "forestgreen", "important");
    });

    // Dark mode toggle
    const darkModeBtn = document.getElementById("darkModeBtn");
    if (darkModeBtn) {
        darkModeBtn.addEventListener("click", function () {
            document.body.classList.toggle("dark-mode");
            const isDarkMode = document.body.classList.contains("dark-mode");
            localStorage.setItem("darkMode", isDarkMode);
            console.log("Dark mode toggled:", isDarkMode);
        });

        // Load dark mode preference
        if (localStorage.getItem("darkMode") === "true") {
            document.body.classList.add("dark-mode");
        }
    }
});
