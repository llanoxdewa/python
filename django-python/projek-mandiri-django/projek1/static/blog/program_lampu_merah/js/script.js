// dom
const lamps = document.querySelectorAll('.lamp');
const active = document.querySelector('.active');
// fungsi stop
function stop(){
    clearInterval(start);
    lamps.forEach(function(lamp){
        lamp.className = 'lamp';
    });
    i = 0;

}
// deklarasi dan initialisasi variabel yang diperlukan
let status = false;
let start;
let i = 0;
active.addEventListener('click',function(){
    // mencek status lampu
    if(status){
        status = false;
        active.textContent = "jalankan";
    }
    else {
        status = true;
        active.textContent = "stop";
    }
    // mencetak status lampu ke console
    console.log((status)? 'lampu nyala':'lampu mati');
    // fungsi untuk menyalakan lampu secara bergilir
    if(status){
       start = setInterval(()=>{
            lamps.forEach(function(lamp){
                lamp.className = 'lamp';
            });
            if(i==lamps.length) i = 0;
            switch ( i ){
                case 0:
                    lamps[i].classList.toggle('red');
                    break;
                case 1:
                    lamps[i].classList.toggle('yellow');
                    break;
                case 2:
                    lamps[i].classList.toggle('green');
                    break;
            }
            i++;
        },200);

    } else {
        // fungsi mematikan
        stop();
    }
});
