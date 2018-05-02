#!/usr/bin/php
<?php

$servername = "globaltec.ec";
$username = "globalte_admin";
$password = "@RbkGlobaltec2017";
$dbname = "globalte_BD_Gevem";

function CallAPI($method, $url, $data = false)
{
	$curl = curl_init();
	switch ($method)
	{
		case "POST":
		curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type: application/x-www-form-urlencoded'));
 		curl_setopt($curl, CURLOPT_POST, 1);
		if ($data)
 			curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
			break;
		case "PUT":
			curl_setopt($curl, CURLOPT_PUT, 1);
			break;
		default:
			if ($data)
			$url = sprintf("%s?%s", $url, http_build_query($data));
	}

	curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
	curl_setopt($curl, CURLOPT_USERPWD, "admin:@Cuco2018");
	curl_setopt($curl, CURLOPT_URL, $url);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
	$result = curl_exec($curl);
	curl_close($curl);
	return $result;
}
$parameters = array ("place"  => "Quito");
$result = CallAPI("POST","http://186.42.174.241/pronostico/tablapred.php?rand=549985337817465","place=Durán");

require('simple_html_dom.php');
$html = str_get_html($result);
$e = $html->find('.table-striped');
$dias = $e[0]->first_child()->first_child()->children();
$hora = $e[0]->first_child()->children(1)->children();
$clima = $e[0]->children(1)->first_child()->children();
$temperatura = $e[0]->children(1)->children(1)->children();
$humedad = $e[0]->children(1)->children(2)->children();
$precipitacion = $e[0]->children(1)->children(3)->children();
$tormenta = $e[0]->children(1)->children(4)->children();

$j = 1;
foreach($dias as $dia)
{
	if(strcmp($dia->plaintext, "Día") !== 0)
	{
		$parts = explode(" ", $dia->plaintext);
		for($i=$j;$i<$j+$dia->colspan;$i++)
		{
			$hr = $hora[$i]->plaintext;		
			$lluvia = trim(preg_replace('/\s+/',' ',$clima[$i]->children(1)->plaintext));
			$temp = str_replace("oC","",$temperatura[$i]->first_child()->first_child()-> plaintext);
			$hum = str_replace("%","",$humedad[$i]->plaintext);
			$prec =  str_replace(",",".",str_replace("mm","",trim(preg_replace('/\s+/','',$precipitacion[$i]->plaintext))));
			$torm = str_replace(",",".",str_replace("%","",$tormenta[$i]->plaintext));
			echo $parts[0].",".$parts[1].",".$hr.",".$lluvia.",".$temp.",".$hum.",".$prec.",".$torm."\n";
		}
		$j+=$dia->colspan;
	}
}

?>
