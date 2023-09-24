
//gets all cupcakes from api.
async function getCupcakes(){
    const cup = await axios.get('http://127.0.0.1:5000/api/cupcakes')
    let cupcakes = cup.data.cupcakes;
 return cupcakes


}
//gets all the cupcakes and inserts them into the webpage
async function showCupcakes(){
let cupcake = await getCupcakes()

for (const cup of cupcake){

const ulElement = document.querySelector('.cup ul');
const li = document.createElement('li')
li.setAttribute('data-id', cup.id)
li.textContent=`Flavor: ${cup.flavor}, Size: ${cup.size}, Rating: ${cup.rating}  `
ulElement.appendChild(li)
}
}

showCupcakes()

const form = document.getElementById("cForm")
//listens for a form submission, and takes the newcupcake, adds it into the db
//and appends it onto the webpage
form.addEventListener("submit", function(e){
    e.preventDefault();

    const flavor = document.getElementById("flavor").value;
    const size = document.getElementById('size').value;
    const rating = document.getElementById('rating').value;
    const image = document.getElementById('image').value;
    console.log(flavor)
    const newCupcake = {
        "flavor": flavor,
        "size": size,
        "rating": rating,
        "image": image
    }
        
    sendnewCupcake(newCupcake);
})

       //fuction that actually adds new cupcake to db     
async function sendnewCupcake(newcp){
      const res = await axios.post('http://127.0.0.1:5000/api/cupcakes', newcp);
      cup = res.data.cupcake;
      addcup(cup)
      return res.data.cupcake;
    
}
//inserts new cupcake into webpage
function addcup(cup){
    const ulElement = document.querySelector('.cup ul');
    const li = document.createElement('li')
    li.setAttribute('data-id', cup.id)
    li.textContent=`Flavor: ${cup.flavor}, Size: ${cup.size}, Rating: ${cup.rating}  `
    ulElement.appendChild(li)
    
}