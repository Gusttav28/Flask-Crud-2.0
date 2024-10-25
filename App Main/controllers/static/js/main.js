const btnEdit = document.querySelectorAll('.btnEdit');
const btnDelete = document.querySelectorAll('.btnDelete');
const btnEditReady = document.querySelectorAll('.btnEditReady');
// const dataUpdating = docuemnt.querySelectorAll('.dataUpdating');
// let number = Number(dataUpdating.value);

if(btnEdit){
    // alert("this is a result from btn edit");
    const btnArray = Array.from(btnEdit);
    btnArray.forEach((btn)=>{
        btn.addEventListener('click', (e)=>{
            if(!confirm("You're going to about to edit this data from the data base table, press OK if you're sure to continue")){
                e.preventDefault();
            }
        })

    })
}
if(btnEditReady){
    // alert("this is a result from btn edit");
    // alert("This is the data that you updated?" + number)
    const btnArray = Array.from(btnEditReady);
    btnArray.forEach((btn)=>{
        btn.addEventListener('click', (e)=>{
            if(!confirm("Are you sure about the changes that you're going to made?")){
                e.preventDefault();
            }
        })
    })
}
if(btnDelete){
    // alert("this is a result from btn edit");
    // alert("This is the data that you updated?" + number)
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn)=>{
        btn.addEventListener('click', (e)=>{
            if(!confirm("Are you sure about to delete this?")){
                e.preventDefault();
            }
        })
    })
}
