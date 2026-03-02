document.addEventListener("DOMContentLoaded", function () {
    const el = document.getElementById("name");
    if (!el) {
        console.error("script.js: element with id 'name' not found");
        return;
    }

    console.log("script.js loaded: attaching click listener to #name");
    el.addEventListener("click", function () {
        console.log("#name clicked");
        this.style.setProperty("color", "blue", "important");
    });
});
