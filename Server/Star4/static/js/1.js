$.ajax({
    type: "GET",
    dataType: "json",
    url: "http://itc-colors.appspot.com/get_images",
    success: function (response) {
        let mypictures=document.getElementById("images");
        for(let i=0;i<response.length;i++)
        {
            var newImg = document.createElement("img");
            newImg.setAttribute('src',response[i])
            mypictures.appendChild(newImg);
        }
    },
    error: function (response) {
        console.log("error");
    },
});