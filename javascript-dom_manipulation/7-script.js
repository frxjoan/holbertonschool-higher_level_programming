const url = "https://swapi-api.hbtn.io/api/films/?format=json";

fetch(url)
    .then(response => response.json())
    .then(data => {
        const filmsList = document.querySelector("#list_movies");
        data.results.forEach(film => {
            const li = document.createElement("li");
            li.textContent = film.title;
            filmsList.appendChild(li);
        });
    })
    .catch(error => {
        console.error("Erreur :", error);
    });
