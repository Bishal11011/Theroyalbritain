
document.addEventListener("DOMContentLoaded", function(){
            
  window.addEventListener('scroll', function() {
     
      if (window.scrollY > 170) {
          document.querySelector('.nav-bar').classList.add('nav-fix');

      } else {
           document.querySelector('.nav-bar').classList.remove('nav-fix');

           // remove padding top from body
      } 
  });
}); 

activeLink()

