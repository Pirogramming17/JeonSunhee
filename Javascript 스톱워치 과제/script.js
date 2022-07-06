const $startBtn = document.querySelector("#start-btn");
const $stopBtn = document.querySelector("#stop-btn");
const $resetBtn = document.querySelector("#reset-btn");
const $records = document.querySelector(".records");
const $curSec = document.querySelector("#sec");
const $curMili = document.querySelector("#mili");
var sec = 0;
var mili = 0;
var time = 0;
var startTime; // 시작 시간
var curTime;
var passedTime;

var startFunc; // 시작 함수

$startBtn.addEventListener("click", function () {
  if (!startTime) {
    startTime = new Date().getTime(); // 새로운 시작 시간 부여
  } else {
    // 재시작 할 때
    var temp = new Date().getTime();
    startTime = new Date(temp - passedTime);
  }

  startFunc = setInterval(function () {
    curTime = new Date().getTime();
    passedTime = new Date(curTime - startTime); // 흐른 시간 = 현재 시간 - 시작시간

    sec = passedTime.getSeconds(); // 흐른 시간 --> 초
    mili = Math.floor(passedTime.getMilliseconds() / 10); // 흐른 시간 --> 밀리 초

    $curSec.innerHTML = String(sec).padStart(2, "0");
    $curMili.innerHTML = String(mili).padStart(2, "0");
  }, 10);
});

$stopBtn.addEventListener("click", function () {
  if (startTime) {
    clearInterval(startFunc);
    $records.innerHTML += `
    <div class="record">
    <input type="checkbox" name="xxx" value="yyy" />
    <span class="record-time">${String(sec).padStart(2, "0")}:${String(
      mili
    ).padStart(2, "0")}</span>
                <span></span>
                </div>
                `;
  }
});

$resetBtn.addEventListener("click", init);

function init() {
  clearInterval(startFunc);
  startTime = null;

  $curSec.innerHTML = "00";
  $curMili.innerHTML = "00";
}
