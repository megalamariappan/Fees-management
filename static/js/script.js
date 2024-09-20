setTimeout(function(){
    document.getElementsByClassName('alert')[0].style.display='none';
},2000)

setTimeout(function(){
    document.getElementById('wrong-user').style.display='none';
},2000)

function addStdValidate(){
    let result = document.getElementsByClassName('valid');
    let regno = document.stdForm.regno.value;

    if(isNaN(regno)){
        result[0].innerHTML = "Enter a valid Regno...!";
    } else {
        result[0].innerHTML = ""; 
    }

    let getaddate=document.stdForm.addate.value;
    let selected_add=new Date(getaddate)
    let currentdate=new Date()
    if(selected_add > currentdate){
        result[1].innerHTML = "The date not might be in future";
    }
    else{
        result[1].innerHTML = "";
    }

    let getdob=document.stdForm.dob.value;
    let selected_dob=new Date(getdob)
    if(selected_dob > currentdate){
        result[2].innerHTML = "The date not might be in future";
    }
    else{
        result[2].innerHTML="";
    }
    let contact = document.stdForm.contact.value;

    if(isNaN(contact)){
        result[3].innerHTML = "Enter a valid Contact Number...!";
    } else {
        result[3].innerHTML = ""; 
    }

    let transportradio=document.stdForm.transport.value;

    if(transportradio == 'Yes'){
        if(!document.getElementById('transportid')){
            inputEl=document.createElement('input');
            inputEl.setAttribute('class','form-control mt-2');
            inputEl.setAttribute('id','transportid');
            inputEl.setAttribute('name','transportfees');
            inputEl.setAttribute('placeholder','Enter Transport Fees');
            let inputdiv=document.getElementsByClassName('transfees');
            inputdiv[0].appendChild(inputEl);
        }
        
    }
    else{
        existinp=document.getElementById('transportid');
        if(existinp){
            existinp.remove()
        }
    }

}
function autosubmit(){
    document.getElementById('detailForm').submit()
}
function automaticsubmit(){
    document.getElementById('reportForm').submit()
}
var modal = document.getElementById("myModal");

  var popup = document.getElementsByClassName('popup');

  // Ensure the popup is found
  if (!popup[0]) {
    console.error('Popup element with ID "popup" not found.');
  }
  
  // Function to open the popup
  function openpopup(feeType,amount) {
    document.getElementById('ftype').value=feeType
    document.getElementById('feeamt').value=amount
    //window.location.href = `/collectFees/${feeType}/`;
    popup[0].classList.add('open-popup');
  }
  
  function closepopup() {
      popup[0].classList.remove('open-popup');
  }
  
  window.onclick = function(event) {
    if (popup[0] && event.target === popup[0]) {
      closePopup();
    }
  }
