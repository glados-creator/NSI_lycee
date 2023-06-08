<?php
include_once("common.php");
$files = glob('images/*.{jpg,png,gif}', GLOB_BRACE);
com_Hstart();
com_Sstart();
?>
<h1 class="center">Simulation</h1> 
  <ul class="inligne">
    <canvas id="can_screen" class="left inline" width="500" height="500"></canvas>
    <ol class="inline" style="vertical-align: baseline;clear: both;">
      <ul style="overflow-y:scroll; clear: both; float: left;" id="can_list">
        <li><h3></h3></li>
      </ul>
      <ol id="img_collect" style="overflow-y:scroll; clear: both; float: right;">
<?php
foreach($files as $file) {
  if (str_contains($file,"icon_")){
    echo "<li>
            <img src=\" $file \" id=\"$file\"/>
          </li>";
}}
?>
        </ol>
      </ol>
</ul>
      <script src="sim.js"></script>
<?php

/// need to load each icons for canvas drawing
com_Send();
com_Hend();
?>