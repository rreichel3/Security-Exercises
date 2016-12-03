<html>
  <head>
    <title>reCAPTCHA demo: Simple page</title>
     <script src="https://www.google.com/recaptcha/api.js" async defer></script>
     <script src="./scripts/captcha.js"></script>
  </head>
  <body>
    <form name="loginForm" action="badcaptchalogin.php" method="post">
        Username: <input type="text" name="username" id="username"/><br>
        Password: <input type="text" name="password" id="password"/><br>
        <p id="instructions">Verify before login. Click Verify then copy the code below into the text field</p>
        <button type="button" id="btn-catpcha" onclick=verify()> Verify</button><br>
        <p id="captcha"></p>
        <input type="text" name="captcha-field" id="captcha-field"></p><br>
        <input type="submit">
        
    </form>
  </body>
</html>