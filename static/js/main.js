"use strict";
console.log("HELLO");
const progressBar = document.querySelector(".progress-bar");
const bodyElement = document.querySelector("body");
const attempts = document.querySelector(".start_range");
const maxAttempts = document.querySelector(".end_range");
progressBar.style.width = `${
  (+attempts.innerHTML / +maxAttempts.innerHTML) * 100
}%`;

bodyElement.addEventListener("keyup", (event) => {
  if (event.code === "Escape") {
    location.reload();
  }
});
