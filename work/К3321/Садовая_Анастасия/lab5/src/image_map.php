<?php 
    require __DIR__ . '/config.php';
    $title = "Интерактивная карта";
    $image_path = "/images/kits.png";
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title><?= $title ?></title>
    <style>
    .map-container {
        position: relative;
        max-width: 800px;
        margin: 20px auto;
    }

    .highlight-box {
        position: absolute;
        border: 3px solid transparent;
        background: rgba(0, 0, 0, 0.2);
        pointer-events: none; /* чтобы не мешал клику по area */
        display: none;
    }
</style>

    

</head>
<body>
    <h1><?= $title ?></h1>
    
    <div class="map-container">
        <img src="<?= $image_path ?>" 
             alt="Интерактивная карта" 
             usemap="#main-map"
             >
        
            <div id="highlight" class="highlight-box"></div>

            <map name="main-map">        

            
            <area shape="rect" coords="215,344,31,8" 
                href="pageOnClick.php" 
                alt="Прямоугольник со ссылкой"
                >
            
            <area shape="circle" coords="334,177,114"
                href="https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0"
                alt="Круг со ссылкой"
                >
            
            <area shape="poly" coords="25,385,79,350,118,363,142,416,218,486,190,543,186,649,151,668,134,634,121,658,87,657,80,580,44,555,59,492,57,449" 
                href="https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%80%D1%81%D0%BA%D0%B8%D0%B5_%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B8" 
                alt="Многоугольник со ссылкой">
    
            <area shape="rect" coords="242,343,442,678" 
                alt="Прямоугольник с выделением"
                onclick="highlightBox(242,343,442,678); return false;">
            
            <area shape="circle" coords="568,526,106" 
                onclick="changeBackground()"
                alt="Круг со сменой фона">
            
            <area shape="poly" coords="535,29,612,36,667,222,607,330,533,325,470,216" 
                onclick="showModal('Информация', 'Вы нажали на котика с карамельным пончиком!'); return false;"
                alt="Многоугольник со всплывающим окном">
                </map>
            </div>
    </div>

    <script>
        function getRandomColor() {
        const r = Math.floor(Math.random() * 256);
        const g = Math.floor(Math.random() * 256);
        const b = Math.floor(Math.random() * 256);
        return `rgba(${r}, ${g}, ${b}, 0.3)`;
        }

        function highlightBox(x1, y1, x2, y2) {
        const box = document.getElementById('highlight');
        const width = x2 - x1;
        const height = y2 - y1;

        const randomColor = getRandomColor();

        box.style.left = x1 + 'px';
        box.style.top = y1 + 'px';
        box.style.width = width + 'px';
        box.style.height = height + 'px';
        box.style.backgroundColor = randomColor;
        box.style.borderColor = randomColor;
        box.style.display = 'block';

        setTimeout(() => box.style.display = 'none', 3000);
        }

        function changeBackground() {
            document.body.style.background = getRandomColor();
        }
        function showModal(title, text) {
            alert(`${title}\n\n${text}`);
        }
    </script>
</body>
</html>