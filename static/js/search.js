function searchFltr() {
    var input, filter, data, searchFilter, timeStamp, i, txtValue;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
    data = document.getElementById("dataSet");
    searchFilter = data.getElementsByClassName("searchFilter");
    for (i = 0; i < searchFilter.length; i++) {
        timeStamp = searchFilter[i].getElementsByClassName("timeStamp")[0];
        txtValue = timeStamp.textContent || timeStamp.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            searchFilter[i].style.display = "";
        } else {
            searchFilter[i].style.display = "none";
        }
    }
}
