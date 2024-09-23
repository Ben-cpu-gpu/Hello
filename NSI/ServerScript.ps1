# Define the server configuration
$serverName = "MyServer"
$serverPort = 8080
$documentRoot = "C:\Server\www"

# Create the server directory
New-Item -Path $documentRoot -ItemType Directory -Force

# Create a sample index.html file
@'
<html>
  <head>
    <title>My Server</title>
  </head>
  <body>
    <h1>Welcome to My Server!</h1>
  </body>
</html>
'@ | Out-File -FilePath "$documentRoot\index.html" -Encoding utf8

# Create the server
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://${serverName}:${serverPort}/")
$listener.Start()

Write-Host "Server started. Listening on http://${serverName}:${serverPort}/"

# Handle incoming requests
while ($listener.IsListening) {
  $context = $listener.GetContext()
  $request = $context.Request
  $response = $context.Response

  Write-Host "Received request: $($request.Url)"

  # Serve the index.html file
  $response.StatusCode = 200
  $response.ContentType = "text/html"
  $response.OutputStream.Write((Get-Content -Path "$documentRoot\index.html" -Encoding utf8), 0, (Get-Content -Path "$documentRoot\index.html" -Encoding utf8).Length)
  $response.OutputStream.Close()
}