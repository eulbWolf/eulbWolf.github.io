<?php

if($_POST["message"]) {
mail("blue9558@gmail.com", "Here is the subject line",
$_POST["message"]. "From: blue9557@gmail.com");

}
?>



