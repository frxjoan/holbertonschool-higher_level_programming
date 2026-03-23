const addBtn = document.querySelector("#add_item");

addBtn.addEventListener("click", function () {
  const ul = document.querySelector("ul.my_list");
  const li = document.createElement("li");
  li.textContent = "Item";
  ul.appendChild(li);
});
