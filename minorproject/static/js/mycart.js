console.log('hello world')
const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultBox = document.getElementById('result-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
// resultBox.innerHTML = ` add a + symbole here to make multiple recommendations
const sendSearchData = (product_name) => {
    $.ajax({
        type:'POST',
        url: '/autocomplete/',
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
                    console.log('this should work multiple times',product_name.pk)
                    resultBox.innerHTML += `
                    <a href = "/product_details/${product_name.pk}">
                        <div class = "row mt-2 mb-2">
                            <div class="col-1">
                                <img src = "${product_name.img}" class ="gam-ing">
                            </div>
                            <div class="col-11">
                                <h5> ${product_name.name} </h5>
                            </div>
                        </div>
                    </a>
                    `
                });
            }
            else{
                if(searchInput.value.length >0){
                    resultBox.innerHTML=resp.data
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

const searchFormmobile = document.getElementById('search-form-mobile')
const searchInputmobile = document.getElementById('search-input-mobile')
const resultBoxmobile = document.getElementById('result-box-mobile')

const csrf1 = document.getElementsByName('csrfmiddlewaretoken')[0].value
// resultBox.innerHTML = ` add a + symbole here to make multiple recommendations
const sendSearchData1 = (product_name) => {
    $.ajax({
        type:'POST',
        url: '/autocomplete/',
        data: {
            'csrfmiddlewaretoken':csrf1,
            'product_name':product_name,
        },
        success: (resp)=> {
            console.log(resp.data)
            const data = resp.data
            if (Array.isArray(data)){
                resultBoxmobile.innerHTML=""
                data.forEach(product_name=> {
                    console.log('this should work multiple times',product_name.pk)
                    resultBoxmobile.innerHTML += `
                    <a href = "/product_details/${product_name.pk}">
                        <div class = "row mt-2 mb-2">
                            <div class="col-2">
                                <img src = "${product_name.img}" class ="gam-ing">
                            </div>
                            <div class="col-10">
                                <h5> ${product_name.name} </h5>
                            </div>
                        </div>
                    </a>
                    `
                });
            }
            else{
                if(searchInputmobile.value.length >0){
                    resultBoxmobile.innerHTML=resp.data
                }
                else{
                    resultBoxmobile.classList.add('not-visible')
                }
            }
        },
        error: (err)=> {
            console.log(err)
        }
    })
}

searchInputmobile.addEventListener('keyup', e=>{
    console.log(e.target.value)

    if(resultBoxmobile.classList.contains('not-visible')){
        resultBoxmobile.classList.remove('not-visible')
    }

    sendSearchData1(e.target.value)
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

$(document).ready(function () {
    $('#btnSubmit1').click(function () {
        $('#myAlert1').show('fade');

        setTimeout(function () {
            $('#myAlert1').hide('fade');
        }, 5000);

    });

    $('#linkClose1').click(function () {
        $('#myAlert1').hide('fade');
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


$(document).ready(function(){
	$(".ajaxLoader").hide();
	// Product Filter Start
	$(".filter-checkbox").on('click',function(){
		var _filterObj={};
        
		$(".filter-checkbox").each(function(index,ele){
			var _filterVal=$(this).val();
			var _filterKey=$(this).data('filter');
			_filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			 	return el.value;
			});
		});
        console.log(_filterObj)
		// Run Ajax
		$.ajax({
			url:'/filter-data',
			data:_filterObj,
			dataType:'json',
			success:function(res){
				console.log(res);
				$("#filteredProducts").html(res.data);
                // console.log(res);
			}
		});
	});
	// End
});