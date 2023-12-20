<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Vulnérabilité SQL injection (à des fins éducatives uniquement)
    $sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";

    if ($username === 'D&dstr0ke77' && $password === 'Epiteqtkek1') {
        echo "Login successful!";
    } else {
        echo "Invalid username or password!";
    }
}
?>
