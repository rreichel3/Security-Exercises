<?php
  require_once('recaptchalib.php');
  $privatekey = "6LdmRw0UAAAAAD4xFHzU2UWsZOxkjFGma_ZEMqk6";
  $resp = recaptcha_check_answer ($privatekey,
                                $_SERVER["REMOTE_ADDR"],
                                $_POST["recaptcha_challenge_field"],
                                $_POST["recaptcha_response_field"]);

  if (!$resp->is_valid) {
    // What happens when the CAPTCHA was entered incorrectly
    die ($_POST["username"] . " login FAILED");
  } else {
    if ($_POST["username"] == "admin") {
      if ($_POST["password"] == "freepass") {
        die ("Access granted!");
      }
      else {
        die ($_POST["username"] . " login FAILED");
      }
    }
    else {
      die ($_POST["username"] . " login FAILED");
    }
    
  }
  ?>