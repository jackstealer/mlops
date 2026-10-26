# Script to run Docker container
Write-Host "Starting Docker container..." -ForegroundColor Green

# Remove existing container if it exists
docker rm -f iris-api 2>$null

# Run the container
$containerId = docker run -d -p 8000:8000 --name iris-api iris-ml-api:v1.0

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Container started successfully!" -ForegroundColor Green
    Write-Host "Container ID: $containerId" -ForegroundColor Cyan
    
    # Wait a moment for startup
    Start-Sleep -Seconds 3
    
    # Show container status
    Write-Host "`nContainer Status:" -ForegroundColor Yellow
    docker ps --filter "name=iris-api"
    
    # Show logs
    Write-Host "`nContainer Logs:" -ForegroundColor Yellow
    docker logs iris-api
    
    Write-Host "`n✅ API is running at: http://localhost:8000" -ForegroundColor Green
    Write-Host "✅ API Documentation: http://localhost:8000/docs" -ForegroundColor Green
    Write-Host "`nTo view logs: docker logs -f iris-api" -ForegroundColor Cyan
    Write-Host "To stop: docker stop iris-api" -ForegroundColor Cyan
} else {
    Write-Host "❌ Failed to start container" -ForegroundColor Red
}
