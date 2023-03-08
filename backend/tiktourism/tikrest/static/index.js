let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  var form = document.createElement('form');
  form.setAttribute('method', 'post');
  form.setAttribute('action', 'updaterecord/' + document.getElementsByClassName("mySlides")[slideIndex].children[1].innerHTML);
  var token = document.createElement('input');
  token.setAttribute('type', 'hidden');
  token.setAttribute('name', '${_csrf.parameterName}');
  token.setAttribute('value', '${_csrf.token}')
  form.appendChild(token)
  form.style.display = 'hidden';
  document.body.appendChild(form)
  form.submit();
  showSlides(slideIndex += n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}