var updateDel = document.getElementsByClassName("update-delivery");
for (let i = 0; i < updateDel.length; i++) {
  updateDel[i].addEventListener("click", function () {
    var assetId = this.dataset.a;
    var action = this.dataset.action;
    var vendor = document
      .getElementsByClassName("dispatch-assets")
      .addEventListener("click", function (e) {
        updateDelivery(assetId, action, vendor);
      });

    console.log("assetId:", assetId, "Action:", action, "vendor:", vendor);

    // check logged in user

    console.log("User:", user);
    if (user == "AnonymousUser") {
      console.log("User is not Authenticated");
    } else {
      console.log("hit");
    //   updateDelivery(assetId, action, vendor);
    }
  });
}
function updateDelivery(assetId, action, vendor) {
  var url = "/assets/update_assets/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ assetId: assetId, action: action, vendor: vendor }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data:", data);
      location.reload();
    });
}
