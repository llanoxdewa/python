
const inputUsername = document.getElementById('username');
const inputPassword = document.getElementById('password');
const inputButton = document.getElementById('login-button');
const boxLogin = document.querySelector('.login-box');


// variabel mengecek apakah username valid / tidak
let usernameIsValid = false;
let passwordIsValid = false;
//mengecek username sudah strong atau low
const validation = {
    username : /[a-zA-Z0-9]{5,15}/,
    password : {
        level_1 : /[a-zA-Z]{5,8}/,
        level_2 : /[a-zA-Z0-9!@#$%^&*()]{8,15}/
    },
};

// event pada username
inputUsername.addEventListener('keyup',() => {
    if(validation['username'].test(inputUsername.value)){
        inputUsername.style.borderColor = 'green';
        usernameIsValid = true;
    } else {
        inputUsername.style.borderColor = 'red';
        usernameIsValid = false;
    }
});

// event pada password
inputPassword.addEventListener('keyup', () => {
    if(validation['password']['level_1'].test(inputPassword.value)){
        inputPassword.style.borderColor = 'yellow';
    }
    if(validation['password']['level_2'].test(inputPassword.value)){
        inputPassword.style.borderColor = 'green';
        passwordIsValid = true;
    }
    if(inputPassword.value == ''){
        inputPassword.style.borderColor = 'red';
        passwordIsValid = false;
    }
});

// mengecek username dan password dan tindakan yang akna dilakuakn
boxLogin.addEventListener('mousemove',() => {
    if(usernameIsValid && passwordIsValid){
        inputButton.classList.remove("warna-for-button-login");
        inputButton.classList.add("efek-for-button-login");
    } else {
        inputButton.classList.remove("efek-for-button-login");
        inputButton.classList.add("warna-for-button-login");
    }
});

// event pada button login
inputButton.addEventListener('click',() => {
    if(usernameIsValid && passwordIsValid){
        window.location.href = "/blog";
    } else {
        alert("username dan password tidak boleh kosong".toUpperCase());
    }
});


