<?php 
    require __DIR__ . '/config.php';
    $title = "Вы кликнули по котику с клубничным пончиком!";
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1><?= $title ?></h1>
        
    <a href="image_map.php">
        <h2>Вернуться к интерактивной карте</h2>
        <img src="/images/kit_flowers.png" 
             alt="Котик с цветочками" 
             width="420" 
             height="550">
    </a>
</body>
</html>
    