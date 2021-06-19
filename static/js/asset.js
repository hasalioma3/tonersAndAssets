
var updateDel = document.getElementsByClassName('update-delivery')
for (let i = 0; i < updateDel.length; i++) {
    updateDel[i].addEventListener('click', function(){
        var assetId = this.dataset.a
        var action = this.dataset.action
        console.log('assetId:', assetId, 'Action:', action)

        // check logged in user

        console.log('User:', user) 
        if (user == 'AnonymousUser') {
            console.log('User is not Authenticated')
        }
        else 
        {
            console.log('hit')
            updateDelivery(assetId, action)
            
        } 
    })
}

function updateDelivery(assetId, action){
    var url = '/assets/update_assets/';
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'assetId': assetId, 'action':action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}