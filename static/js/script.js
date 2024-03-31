

async function getRooms () {
    let formData = new FormData();
    let _arr = document.getElementById("arrive_date").value;
    formData.append("arr", _arr);
     let response = await fetch("http://192.168.1.11:5000/api/v1.0/show_rooms",
            {
                method: "POST",
                body: formData
            });
     let result = await response.json();
}


document.getElementById("show_rooms_btn").addEventListener("click", async () => {
    let v = document.getElementById("date-select").value;
    let formData = new FormData();
    formData.append("date", v);
    let response = await fetch("http://192.168.1.11:5000/api/v1.0/show_rooms",
            {
                method: "POST",
                body: formData
            });
     let result = await response.json();

})

