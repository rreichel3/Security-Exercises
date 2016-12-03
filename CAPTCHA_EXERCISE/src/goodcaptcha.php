<html>
  <head>
    <title>reCAPTCHA demo: Simple page</title>
     <script src="https://www.google.com/recaptcha/api.js" async defer></script>
  </head>
  <body>
    <form name="loginForm" action="goodcaptchalogin.php" method="post">
        Username: <input type="text" name="username" id="username"/><br>
        Password: <input type="text" name="password" id="password"/><br>
        <?php 
        require_once('recaptchalib.php');
        $publickey = "6LdmRw0UAAAAAFhMcS50q62qbM4izOpexdCslD3w"; // you got this from the signup page
        echo recaptcha_get_html($publickey);
        ?>
        <input type="submit">
    </form>
  </body>
</html>