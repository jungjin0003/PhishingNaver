let TIME = 180;
let TIMER;

function StartTimer()
{
    TIME = 180;
    StopTimer();
    window.qrImageDiv.style.display = "block";
    window.reloadGuide.style.display = "none";
    TIMER = setInterval(UpdateTimer, 1000);
}

function StopTimer()
{
    clearInterval(TIMER);
}

function UpdateTimer()
{
    TIME--;
    let seconds = Math.floor(TIME % 60);
    let minutes = Math.floor(TIME / 60);
    time = '0' + minutes + ':';
    time += seconds < 10 ? '0' + seconds : seconds;
    window.timeStamp.innerText = time;
    if (TIME == 0)
    {
        window.qrImageDiv.style.display = "none";
        window.reloadGuide.style = "block";
        StopTimer();
    }
}