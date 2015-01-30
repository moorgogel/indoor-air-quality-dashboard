<?php
require_once ("Carbon/Carbon.php");
use Carbon\Carbon;

$background_state=0;
$ts_arr = array_fill(0, 24, NULL);
$name_arr = array_fill(0, 24, NULL);

$result=mysqli_query($conn,"SELECT * from state_type where location_id=$location_id order by name");

echo "<h3 style='clear:left;'>States</h3>";
echo "<table border=0>";
while($row = mysqli_fetch_array($result)) {
  echo get_event_row($row['name']);  
}
echo "</table>\n"; 
echo "<img src='images/add.png' onclick='location.href=\"events/manage_states.php?id=$id&location_id=$location_id&start_date=".$start_date_param."&size=".$size."\"' height=30 width=30 style='cursor:pointer;'>";

/*
if(isset($row['name'])) $background_state=1;

$result=mysqli_query($conn,"SELECT * from events where ts>=$start_day_utc and ts<$end_day_utc and core_id=$id order by ts");
while($row = mysqli_fetch_array($result)) {
  $event_ts = Carbon::createFromTimeStamp($row['ts']);
  $event_hour = $event_ts->format('G');
  $ts_arr[$event_hour] = $event_ts;
  $name_arr[$event_hour] = $row['name'];
}
*/

// --------------------------------------------------------------------- FUNCTIONS
function get_event_row($name) {
  global $date;
  
  $html="";
  $html.="<tr>";
  $html.="<th style='text-align:right;'>$name</th>";
  for($i=0;$i<24;$i++) {
    $background='';
    if(isset($ts_arr[$i])) {
      if(!isset($name_arr[$i])) {
        $background_state=0;
      } else if($background_state==1) {
        $background_state=2;
      } else {
        $background_state=1;
      }
    }
    if($background_state==1) {
      $background='background-color:#CC6666;';
    } else if($background_state==2) {
      $background='background-color:#3399CC;';
    }  
    $curr_ts_utc=$date->copy()->startOfDay()->addHours($i)->format('U');
    $html.="<td style='text-align:center;font-size:11px;width:40px;cursor:pointer;border:1px solid purple;$background' ";
    $html.="onclick='location.href=\"events/manage_event.php?id=$id&ts=$curr_ts_utc"."&start_date=".$start_date_param."&size=".$size."\"'>";
    $html.=sprintf("%1$02d",$i);
    $html.="</td>";
  
  }
  $html.="</tr>";
  return $html;
}
?>