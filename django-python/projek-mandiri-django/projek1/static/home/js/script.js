const toBlog = document.querySelector('.blog');
const toLogin = document.querySelector('.login');


toBlog.addEventListener('click',()=>{
    window.location.href = "/blog";
});

toLogin.addEventListener('click',() => {
    window.location.href = "/login";
});

