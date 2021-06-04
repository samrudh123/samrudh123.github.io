<%
dim username,email,password
username=Request.Form("username")
email=Request.Form("email")
password=Request.Form("password")
Response.Write("Username: " & username)
Response.Write("Email: " & email)
Response.Write("Password: " & password)
%>