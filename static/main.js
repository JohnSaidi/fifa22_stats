function searchPage() {
    if(document.getElementById("searchinput").value === "") {
        document.getElementById('searchbtn').disabled = true;
    }else {
        document.getElementById('searchbtn').disabled = false;
    }
}

function comparePage() {
    if(document.getElementById("compareinput").value === "") {
        document.getElementById('comparebtn').disabled = true;
    }else {
        document.getElementById('comparebtn').disabled = false;
    }
}
