const $ideaInterest = document.getElementsByClassName("idea-interest");
var $plusBtn = [];
var $minusBtn = [];
var $interest = [];
for (var i = 0; i < $ideaInterest.length; i++) {
  $plusBtn[i] = $ideaInterest.getElementsByClassName("plus-btn")[i];
  $interest[i] = $ideaInterest.getElementsByClassName("interest")[i];
  $minusBtn[i] = $ideaInterest.getElementsByClassName("minus-btn")[i];

  $plusBtn[i].addEventListener("click", function () {
    var temp = parseInt($interest[i].innerText) + 1;
    $interest[i].innerText = temp;
  });
  $minusBtn[i].addEventListener("click", function () {
    var temp = parseInt($interest[i].innerText) - 1;
    $interest[i].innerText = temp;
  });
}
