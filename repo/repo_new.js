function checkName(){
    var name = document.getElementById('name').value;
    if(name.length < 8){
      alert('8文字以上入力してください'); 
    }
  }