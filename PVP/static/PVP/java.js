function history() {
    let URLLiElement = document.createElement("li");
    var input = document.getElementById("in").value;
    localStorage.setItem("url",input);
    document.getElementById("hist").appendChild(URLLiElement);
}




function add() {
    let URLLiElement = document.createElement("li");
    URLLiElement.setAttribute("class", "list-group-item d-flex justify-content-between");
    URLLiElement.innerHTML = "video";
    document.getElementById("bookmarks").appendChild(URLLiElement);
}
