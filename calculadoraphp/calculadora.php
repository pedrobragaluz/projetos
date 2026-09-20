<?php
   $n1 = $_POST['numero1'];
   $n2 = $_POST ['numero2'];
   $operacao = $_POST['opercao'];

   if ($operacao == "soma") {
    $resultado = $n1 + $n2;

   } elseif ($operacao == "subtracao") {
    $resultado = $n1 - $n2;

   } elseif($operacao == "multiplicacao") {
    $resultado = $n1 * $n2;

   } elseif ($operacao == "divisao") {
    $resultado = $n1 / $n2;
   }

   echo "O resultado é: " . $resultado;
?>



   