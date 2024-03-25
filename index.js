// This is JS code for PDF download
function downloadAsPDF() {
    let element = document.querySelector(".resume-container");
    html2pdf().from(element).save("ivan.kotromanovic.pdf");


}

// This is JS code for visitor counter update
const counter = document.querySelector(".counter-number");
async function updateCounter() {
    //let response = await fetch("https://igljedisu3pcqqepwigchjb73m0qfgsp.lambda-url.us-east-1.on.aws/");
    let response = await fetch("https://p44klqatbb.execute-api.us-east-1.amazonaws.com/Prod");
    let data = await response.json();
    counter.innerHTML = `Site views:${data.views}`;
}

updateCounter();

