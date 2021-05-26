$(document).ready(function () {
    $('#btnSubmit').click(function () {
        $('#myAlert').show('fade');

        setTimeout(function () {
            $('#myAlert').hide('fade');
        }, 5000);

    });

    $('#linkClose').click(function () {
        $('#myAlert').hide('fade');
    });
});

// window.setTimeout(function() {
//     $(".alert").fadeTo(500, 0).slideUp(500, function(){
//         $(this).remove(); 
//     });
// }, 2000);

$('.itee').click(function() {
    $('#myAlert').show('fade');

        setTimeout(function () {
            $('#myAlert').hide('fade');
        }, 2000);
    
    var id = $(this).attr("pid").toString();
    console.log(id)

    $.ajax({
        type:"GET",
        url:"/add_to_cart",
        data:{
            prod_id: id
        },
        success: function(data){
            console.log(data)
            console.log("Success")
            document.getElementById("totalpurchased1").innerText = data.totalpurchased
        }
    })
})

$('.up').click(function() {
    var id = $(this).attr("pid").toString();
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/add_to_cart",
        data:{
            prod_id: id
        },
        success: function(data){
            // console.log(data)
            // console.log("Success")
            document.getElementById(id).value = data.quantity
            document.getElementById('totalpurchased1').innerText = data.totalpurchased
            document.getElementById('totalpurchased2').innerText = "Rs." + data.amount + "/-"
            document.getElementById('totalpurchased3').innerText = "Rs." + data.amount + "/-"  
        }
    })
})

$('.down').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this
    // console.log(id)

    $.ajax({
        type:"GET",
        url:"/minus_cart",
        data:{
            prod_id: id
        },
        success: function(data){
            // console.log(data)
            // console.log("Success")
            document.getElementById(id).value = data.quantity
            document.getElementById('totalpurchased1').innerText = data.totalpurchased
            document.getElementById('totalpurchased2').innerText = "Rs." + data.amount + "/-"
            document.getElementById('totalpurchased3').innerText = "Rs." + data.amount + "/-"
            if(data.quantity<=0)
                eml.parentNode.parentNode.parentNode.remove()
        }
    })
})

$('.remove-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this
    // console.log(id)

    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id: id
        },
        success: function(data){
            // console.log(data)
            // console.log("Success")
            // document.getElementById(id).value = data.quantity
            document.getElementById('totalpurchased1').innerText =  data.totalpurchased
            document.getElementById('totalpurchased2').innerText = "Rs." + data.amount + "/-"
            document.getElementById('totalpurchased3').innerText = "Rs." + data.amount + "/-"
            eml.parentNode.parentNode.remove()
        }
    })
})
