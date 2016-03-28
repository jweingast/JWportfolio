var lst = document.getElementsByTagName('li');
for(var i = 0; i < lst.length; i++){
    lst[i].onclick=function(){
        if(this.parentNode){
            var childList = this.parentNode.getElementsByTagName('UL');
            for(var j = 0; j< childList.length;j++){
                var currentState = childList[j].style.display;
                if(currentState=="none"){
                    childList[j].style.display="block";
                }else{
                    childList[j].style.display="none";
                }
            }
        }
    }
}
