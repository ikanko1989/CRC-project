//fetch function for site views
const counter = document.querySelector(".counter-number");
async function updateCounter() {
    let response = await fetch("arn:aws:lambda:us-east-1:767397953558:function:updateDatabaseCounter");
    let data = await response.json();
    counter.innerHTML = ` This page has ${data} Views!`;
}

updateCounter();



