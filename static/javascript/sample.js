
function dispText() {
    var text = document.anc.check.value + "','" +
        my_dict.type + "','" ;
    var blob = new Blob([text], { "type": "text/plain" });

    //IEの場合
    if (window.navigator.msSaveBlob) {
        window.navigator.msSaveBlob(blob, "outFileFromWindows.txt");
        //IE以外の場合
    } else {
        document.getElementById("createFile").href = window.URL.createObjectURL(blob);
    }
}