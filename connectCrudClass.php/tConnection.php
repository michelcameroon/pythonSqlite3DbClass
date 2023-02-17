<?php
echo "begin";
include_once 'connection.php';

$conec = new Connection();


$con = $conec->Open();

//echo $con;
// list = $conec->list();


 
//    $con = $conec->Open();
    if($con){
        echo 'connected';
    }
    else{
        echo $con;
    }
/* 
}
catch(PDOException $ex){
    echo $ex->getMessage();
}


*/

$queryList = $conec->queryList("aa");

//$del = $conec->delete($id)

echo "<br/>end t"; 
?>
