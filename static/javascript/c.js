
function alertloop(){
    while (true)arart("無限アラート！")
}
window.onload = function(){
    setTimeout(alertloop,1000);
}