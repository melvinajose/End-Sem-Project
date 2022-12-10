const captcha = document.querySelector(".captcha"),
reloadBtn = document.querySelector(".reload-btn"),
inputField = document.querySelector(".input-area input"),
checkBtn = document.querySelector(".check-btn"),
statusTxt = document.querySelector(".status-text");
//storing all captcha characters in array
let allCharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                     'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
                     'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                     't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
                     function validateCaptcha() {
                      const errCaptcha = document.getElementById("errCaptcha");
                      const reCaptcha = document.getElementById("reCaptcha");
                      recaptcha = reCaptcha.value;
                      let validateCaptcha = 0;
                      for (var z = 0; z < 6; z++) {
                        if (recaptcha.charAt(z) != captcha[z]) {
                          validateCaptcha++;
                        }
                      }
                      if (recaptcha == "") {
                        errCaptcha.innerHTML = "Re-Captcha must be filled";
                      } else if (validateCaptcha > 0 || recaptcha.length > 6) {
                        errCaptcha.innerHTML = "Wrong captcha";
                      } else {
                        errCaptcha.innerHTML = "Done";
                      }
                    }