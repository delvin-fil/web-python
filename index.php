<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="favicon.png" type="image/x-icon"/>
<link rel="stylesheet" type="text/css" href="my.css" />
<title><?php 
date_default_timezone_set('Asia/Krasnoyarsk');
echo date('d-n-y H:m'); 
?></title>
</head>
<body>
    <div id="header">
        <?php         require_once ('header.php');
        ?>
    </div>
<div id="content">
<br><br><br><br>
<p> Если вы можете прочитать этот текст, значит ваш веб-сервер работает и настроен правильно. </p>
<a href="index.py">Здесь Python</a><br>
<form method = "post">
<input type = "submit" name = "sort" value = "Показать инфу о PHP">
<input type = 'submit' name = 'hid' value = 'Скрыть нахуй!'>
</form>

<?php
if (isset($_POST['sort'])) // если кнопка  'order' нажата 
{
	echo "Во, бля! 😎";
    phpinfo();
}
if (isset($_POST['hid']))
{
echo "ЕПТ! 😈\r\n";
} 
?>
</div>


</body>
</html>