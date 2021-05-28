// $(function () {
//     $("#product").autocomplete({
//         source: ['js','python','php']
//     });
// });

// $(function () {
//     $("#product2").autocomplete({
//         source: ['js','python','php']
//     });
// });

// $(function () {
//     $("#product3").autocomplete({
//         source: ['js','python','php']
//     });
// });

console.log('hello world')
const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultBox = document.getElementById('result-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData = (product_name) => {
    $.ajax({
        type:'POST',
        url: 'autocomplete/',
        data: {
            'csrfmiddlewaretoken':csrf,
            'product_name':product_name,
        },
        success: (resp)=> {
            console.log(resp.data)
            const data = resp.data
            if (Array.isArray(data)){
                resultBox.innerHTML=""
                data.forEach(product_name=> {
                    resultBox.innerHTML = `
                    <a href = "${url}product_details/${product_name.pk}" class = "">
                        <div class = "row mt-2 mb-2">
                            <div class="col-2">
                                <img src = "${product_name.img}" class ="gam-ing">
                            </div>
                            <div class="col-10">
                                <h5> ${product_name.name} </h5>
                            </div>
                        <div>
                    `
                })
            }
            else{
                if(searchInput.value.length >0){
                    resultBox.innerHTML=`<b></b>`
                }
                else{
                    resultBox.classList.add('not-visible')
                }
            }
        },
        error: (err)=> {
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value)

    if(resultBox.classList.contains('not-visible')){
        resultBox.classList.remove('not-visible')
    }

    sendSearchData(e.target.value)
})

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
