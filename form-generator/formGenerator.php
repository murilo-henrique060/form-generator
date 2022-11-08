<!DOCTYPE html>
<html>
    <title>
        Form generator
    </title>
    <body>
    <?php
        $cName = "config.json";
        $form = json_decode(file_get_contents($cName), true);

        echo "<h1>$form[title]</h1>\n";

        function text($text) {
            echo "<p>$text</p>\n";
        }

        function label($question, $id, $name = null) {

            if ($name === null) {
                $name = $id;
            }

            echo "<label for=$id>$question</label><br>\n";
            echo "<input type=text id=$id name=$name>\n";
        }

        function radio($question, $name, $options) {
            echo "<p>$question</p>";
            foreach($options as $op) {
                echo "<input type=radio id=" . $op["id"] . " name=$name  value=" . $op["value"] . ">";
                echo "<label for=$name>" . $op["content"] . "</label>";
            }
        }

        $cont = 0;
        echo "<form>";
        foreach($form["func"] as $f) {
            echo "<h2>Question" . $cont + 1  . "</h2>\n";
            call_user_func_array($f, $form["args"][$cont]);
            $cont++;
        }
        echo "</form>";
    ?>
    </body>
</html>