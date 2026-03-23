const updBtn = document.querySelector("#update_header");

updBtn.addEventListener("click", function () {
    const header = document.querySelector("header");
    header.textContent = "New Header!!!";
});
