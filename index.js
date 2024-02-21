// This is JS code for PDF download
function downloadAsPDF(){
    let element=document.querySelector(".resume-container");
    html2pdf().from(element).save("ivan.kotromanovic.pdf");
    

}

// This is JS code for visitor counter
