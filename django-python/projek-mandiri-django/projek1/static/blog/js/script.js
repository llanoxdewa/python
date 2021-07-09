
const h1TopBar = document.querySelector('.topbar h1');
const tulisanKece = document.querySelector('.tulisan-kece');
const kotakPilihan = document.




let idx = 0;

let status = false;
let kata = "selamat datang di blog";

setInterval(()=>{
    let kalimat = kata.split('').
    map((char,i) => (i===idx && char != ' ')? `<span class='efek-kece'>${char}</span>`:char);
    h1TopBar.innerHTML = kalimat.join('');

    if(!status)
        idx++;
    else
        idx--;
    if(idx == kata.length){
        status = true;
        idx--;
    }
    else if(idx === 0)
        status = false;
},200);



let idx2 = 0;
let kataForTulisanKece = "silahkan melihat projek yang pernah dibuat"

setInterval(() => {
    let kalimats = kataForTulisanKece.split(' ')
    .map((kalimat,i) => (i === idx2)? `<span class="efek-tulisan-kece">${kalimat}</span>` : kalimat);
    tulisanKece.innerHTML = kalimats.join(' ');
    idx2++;
    if(idx2 == kalimats.length){
        idx2 = 0;
    }
    console.log(idx2);
},500);
