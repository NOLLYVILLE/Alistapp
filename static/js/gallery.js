var ProducImg = document.getElementById("ProductImg");
var smalling = document.getElementsByClassName("SmallImg");

    Smalling[0].onclick = function()
    {
        ProductImg.src = Smalling[0].src;
    }
    Smalling[1].onclick = function()
    {
        ProductImg.src = SmallImg[1].src;
    }
    SmallImg[2].onclick = function()
    {
        ProductImg.src = SmallImg[2].src;
    }
    SmallImg[3].onclick = function()
    {
        ProducImg.src = SmallImg[3].src;
    }