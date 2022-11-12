let cirProgress = document.querySelector(".circle"),
progressvalue=document.querySelector(".progress-value");

let progressStartValue = 0,
    progressEndValue = 50,
    speed =100;

let progress = setInterval(() =>{
    progressStartValue++;

    progressvalue.textContent = `${progressStartValue}%`
    cirProgress.style.background =`conic-gradient(blueviolet  ${progressStartValue * 3.6}deg,#ededed 0deg)`

    if(progressStartValue == progressEndValue){
        clearInterval(progress)
    }
    console.log(progressStartValue);
},speed);
