"use strict";
console.log("HELLO");
// const startRange = 100;
// const endRange = 140;
// let historyNumber = [];
// let randomNumber = Math.round(
//   startRange + Math.random() * (endRange - startRange)
// );
// let maxAttempts = Math.ceil(Math.log2(endRange - startRange + 1));
// let attempts = Math.ceil(Math.log2(endRange - startRange + 1));
// const getNumberInput = document.querySelector(".enter__number");
// const getCheckNumberBtn = document.querySelector(".check__btn");
// const getHistoryBlock = document.querySelector(".history__list");
// const getNewNumberBtn = document.querySelector(".new__number__btn");
const progressBar = document.querySelector(".progress-bar");
// const mainDashboard = document.querySelector(".table");
// const restartDashboard = document.querySelector(".table__result");
// const resultMessage = document.querySelector(".result__subtitle");
// const restartGameBtn = document.querySelector(".restart__btn");
const bodyElement = document.querySelector("body");
const attempts = document.querySelector(".start_range");
const maxAttempts = document.querySelector(".end_range");
progressBar.style.width = `${((+attempts.innerHTML) / (+maxAttempts.innerHTML)) * 100}%`;
// console.log(randomNumber);
// console.log(`Tries: ${attempts}`);
// function checkNumber() {
//   if (
//     getNumberInput.value &&
//     +getNumberInput.value >= startRange &&
//     +getNumberInput.value <= endRange
//   ) {
//     --attempts;
//     historyNumber.push(
//       `<span>${+getNumberInput.value < randomNumber ? ">" : "<"}${
//         getNumberInput.value
//       }</span>`
//     );
//     getHistoryBlock.innerHTML = historyNumber.toString();
// progressBar.style.width = `${(attempts / maxAttempts) * 100}%`;
//     if (randomNumber == +getNumberInput.value || attempts == 0) {
//       mainDashboard.style.display = "none";
//       restartDashboard.style.display = "block";
//       resultMessage.innerHTML = `Вы ${
//         randomNumber == +getNumberInput.value ? "победили" : "проиграли"
//       }, загаданное число было: ${randomNumber}`;
//       restartGameBtn.focus();
//     }
//     getNumberInput.value = "";
//     getNumberInput.focus();
//     errorMsg.style.display = "none";
//   } else {
//     errorMsg.style.display = "block";
//   }
// }

// function restartGame() {
//   historyNumber = [];
//   errorMsg.style.display = "none";
//   getNumberInput.value = "";
//   getHistoryBlock.innerHTML = "";
//   randomNumber = Math.round(
//     startRange + Math.random() * (endRange - startRange)
//   );
//   attempts = Math.log2(endRange - startRange + 1).toFixed();
//   progressBar.style.width = "100%";
//   mainDashboard.style.display = "block";
//   restartDashboard.style.display = "none";
//   getNumberInput.focus();
// }

// function newNumber() {
//   historyNumber = [];
//   getNumberInput.value = "";
//   getHistoryBlock.innerHTML = "";
//   progressBar.style.width = "100%";
//   randomNumber = +(Math.random() * 100).toFixed();
//   console.log(randomNumber);
//   getNumberInput.focus();
//   attempts = Math.log2(endRange - startRange + 1).toFixed();
// }

// getCheckNumberBtn.addEventListener("click", () => {
//   checkNumber();
// });

// getCheckNumberBtn.addEventListener("keyup", (event) => {
//   if (event.code === "Enter") {
//     checkNumber();
//   }
// });

// getNewNumberBtn.addEventListener("keyup", (event) => {
//   if (event.code === "Enter") {
//     newNumber();
//   }
// });

// getNewNumberBtn.addEventListener("click", () => {
//   newNumber();
// });

// restartGameBtn.addEventListener("click", () => restartGame());
// restartGameBtn.addEventListener("keyup", (event) => {
//   if (event.code === "Enter") {
//     restartGame();
//   }
// });

bodyElement.addEventListener("keyup", (event) => {
  if (event.code === "Escape") {
    // restartGame();
    location.reload();
  }
});

// getNumberInput.addEventListener("keyup", (event) => {
//   if (event.code === "Enter") {
//     checkNumber();
//   }
// });
