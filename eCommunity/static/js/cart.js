var buttons = document.getElementsByClassName('change-cart')

for(var i = 0; i < buttons.length; i++){
  buttons[i].addEventListener('click', function(){
    var product = this.dataset.product
    var action = this.dataset.action
    console.log('product:', product, 'action:', action)

    console.log('USER:', user)
    if (user === 'AnonymousUser'){
      console.log('Not logged in')
    }else{
      updateUserOrder(product, action)
    }
  })
}


function updateUserOrder(product, action){
  var url = '/update_item/'

  fetch(url, {
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken
    },
    body:JSON.stringify({'product': product, 'action': action})
  })

  .then((response)=>{
    return response.json()
  })

  .then((data)=>{
    console.log('data:', data)
    location.reload()
  })
}
