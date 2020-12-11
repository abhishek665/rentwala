  function w3_open() {
    document.getElementById("main").style.marginLeft = "25%";
    if (screen.width < 600){
      document.getElementById("mySidebar").style.width = "50%";
    }
    else{
      document.getElementById("mySidebar").style.width = "30%";
    }
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("openNav").style.display = 'none';
  }
  function w3_close() {
    document.getElementById("main").style.marginLeft = "0%";
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("openNav").style.display = "inline-block";
  }
  function myAccFunc() {
    var x = document.getElementById("demoAcc");
    var Icon = document.getElementById('Accordion_Icon');
    console.log(Icon)
    if (x.className.indexOf("w3-show") == -1) {
      x.className += " w3-show";
      Icon.setAttribute('class', 'fa fa-caret-up');
    } else { 
      x.className = x.className.replace(" w3-show", "");
      x.previousElementSibling.className = 
      x.previousElementSibling.className.replace(" w3-green", "");
      Icon.setAttribute('class', 'fa fa-caret-down');
    }
  }
  function myAccFunc2() {
    var x = document.getElementById("demoAcc2");
    var Icon = document.getElementById('Accordion_Icon2');
    console.log(Icon)
    if (x.className.indexOf("w3-show") == -1) {
      x.className += " w3-show";
      Icon.setAttribute('class', 'fa fa-caret-up');
    } else { 
      x.className = x.className.replace(" w3-show", "");
      x.previousElementSibling.className = 
      x.previousElementSibling.className.replace(" w3-green", "");
      Icon.setAttribute('class', 'fa fa-caret-down');
    }
  }
  function myAccFunc3() {
    var x = document.getElementById("demoAcc3");
    var Icon = document.getElementById('Accordion_Icon3');
    console.log(Icon)
    if (x.className.indexOf("w3-show") == -1) {
      x.className += " w3-show";
      Icon.setAttribute('class', 'fa fa-caret-up');
    } else { 
      x.className = x.className.replace(" w3-show", "");
      x.previousElementSibling.className = 
      x.previousElementSibling.className.replace(" w3-green", "");
      Icon.setAttribute('class', 'fa fa-caret-down');
    }
  }