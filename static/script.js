const dropArea = document.getElementById("dropArea");
const fileInput = document.getElementById("fileInput");

dropArea.addEventListener("click", () => {

fileInput.click();

});

dropArea.addEventListener("dragover", (e) => {

e.preventDefault();
dropArea.style.background = "#334155";

});

dropArea.addEventListener("dragleave", () => {

dropArea.style.background = "transparent";

});

dropArea.addEventListener("drop", (e) => {

e.preventDefault();

const files = e.dataTransfer.files;

fileInput.files = files;

});