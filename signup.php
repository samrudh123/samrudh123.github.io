<html>
<body>
<?php

function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

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

$stmt = $conn->prepare("INSERT INTO VolleyballUserLogin (username, email, password) VALUES (?, ?, ?)");
$stmt->bind_param("sss", $username, $email, $password);

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $username = test_input($_POST["username"]);
    $email = test_input($_POST["email"]);
    $password = test_input($_POST["password"]);
    $stmt->execute();
    }

$stmt->close();

$sqlq = "SELECT id, username, email, password FROM VolleyballUserLogin";
$result = $conn->query($sqlq);

if ($result->num_rows > 0) {
  // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<br>" . "id: " . $row["id"]. "<br>" . " Username: " . $row["username"]. "<br> " . "Email: " . $row["email"]. "<br>" . "Password: " . $row["password"] . "<br>";
  }
} else {
    echo "<br>" . "0 results";
}


// sql to delete a record
$sqld = "DELETE FROM VolleyballUserLogin WHERE password=''";

if ($conn->query($sqld) === TRUE) {
    //echo "<br>" . "Records deleted successfully";
} else {
    echo "<br>" . "Error deleting record: " . $conn->error;
}

$conn->close();

?>
</body>
</html>