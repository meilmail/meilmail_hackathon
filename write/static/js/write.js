var textarea = document.querySelector("textarea[name='content']");
var input = document.querySelector("input[name='title']");

function changeFont() {
  let select = document.querySelector("select[name='font']");
  let options = select.options;

  textarea.style.fontFamily = options[select.selectedIndex].value;
  input.style.fontFamily = options[select.selectedIndex].value;
}

function changeSize() {
  let select = document.querySelector("select[name='size']");
  let options = select.options;

  textarea.style.fontSize = options[select.selectedIndex].value;
}

function changeAlign() {
  let select = document.querySelector("select[name='align']");
  let options = select.options;

  textarea.style.textAlign = options[select.selectedIndex].value;
}