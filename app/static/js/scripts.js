var switcher = document.querySelectorAll(".switcher")
console.log(document.que)
switcher.forEach((element) =>{
    element.addEventListener("click", function(){
        if (element.hasChildNodes){
            console.log(this.childNodes)
            line1 = element.childNodes[1]
            line2 = element.childNodes[3]
            element.classList.toggle("active")
            line1.classList.toggle("x")
            line2.classList.toggle("y")
            console.log(this)
            let content = this.parentNode.parentNode.querySelector('.variant__content')
            content.classList.toggle("active")
            // console.log(content.style)
            // if (content.style.display=='block'){
            //     content.style.display=='none'
            //     content.style.maxHeight = null
            //     console.log("Null")
            // }
            // else{
            //     console.log("Scroll")
            //     content.style.display=='block'
            //     content.style.maxHeight = 50
            // }
        }
    })
})

