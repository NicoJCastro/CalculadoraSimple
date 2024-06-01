let display = document.getElementById('display');

function appendToDisplay(value){
    if (display.innerText === "0" || display.innerText == "Error") {
        display.innerText = value;
    }else {
        display.innerText += value;
    }
}

function clearDisplay(){
    display.innerText = "0";
}   

function deleteLast(){
    display.innerText = display.innerText.slice(0, -1);
}

function calculateResult(){
    try {
        display.innerText = eval(display.innerText);
    } catch {
        display.innerText = "Error";
    }
}

function calculatePercentage(){
    try {
        display.innerText = eval(display.innerText) / 100;
    } catch {
        display.innerText = "Error";
    }
    console.log(display.innerText);
}