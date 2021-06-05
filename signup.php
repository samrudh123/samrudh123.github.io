<html>
<body>
<?php

define("DB_HOST", "localhost");
define("DB_USER", "root");
define("DB_PASSWORD", "");
define("DB_DATABASE", "myDB");

// Create connection
$conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$username = $email = $password = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $username = test_input($_POST["username"]);
  $email = test_input($_POST["email"]);
  $password = test_input($_POST["password"]);
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

$sql = "INSERT INTO LoginDatabase (username, email, password)
VALUES ('$username', '$email', '$password')";


if ($conn->query($sql) === TRUE) {
  $last_id = $conn->insert_id;
  echo "<br>" . "New record created successfully. Last inserted ID is: " . $last_id . "<br>";
} else {
  echo "<br>" . "Error: " . $sql . "<br>" . $conn->error;
}

$sqlq = "SELECT id, username, email, password FROM LoginDatabase";
$result = $conn->query($sqlq);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "<br>" . "id: " . $row["id"]. "<br>" . " Username: " . $row["username"]. "<br> " . "Email: " . $row["email"]. "<br>" . "Password: " . $row["password"];
  }
} else {
  echo "<br>" . "0 results";
}


/*
// sql to delete a record
$sqld = "DELETE FROM LoginDatabase";

if ($conn->query($sqld) === TRUE) {
  echo "<br>" . "<br>" . "Record deleted successfully";
} else {
  echo "<br>" . "Error deleting record: " . $conn->error;
}
*/

$conn->close();
?>
</body>
</html>