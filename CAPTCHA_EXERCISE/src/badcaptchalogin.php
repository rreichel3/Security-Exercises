<?php
  if ($_POST["captcha-field"] == "DOG CAT") {
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
  } else {
    die ($_POST["username"] . " login FAILED");
  }
  ?>  