function clickInput() {
  let el = document.querySelector("input[type='file']");
  el.click();
}

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      document.querySelector('.writer_info_top_thumbnail_img').innerHTML = '<img src="" />';
      document.querySelector('.writer_info_top_thumbnail_img img').setAttribute('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
  }
}

function changeThumbnail() {
  readURL(document.querySelector("input[type='file']"));
}