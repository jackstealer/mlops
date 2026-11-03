# Remove existing container if it exists
Write-Host "Removing old container if exists..." -ForegroundColor Yellow
docker rm -f iris-api 2>$null

# Run the container
Write-Host "Starting iris-api container..." -ForegroundColor Green
$containerId = docker run -d -p 8000:8000 --name iris-api iris-ml-api:v1.0

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Container started successfully!" -ForegroundColor Green
    Write-Host "Container ID: $containerId" -ForegroundColor Cyan
    
    # Wait for container to start
    Start-Sleep -Seconds 3
    
    # Show container status
    Write-Host "`n📊 Container Status:" -ForegroundColor Yellow
    docker ps --filter "name=iris-api"
    
    # Show logs
    Write-Host "`n📝 Container Logs:" -ForegroundColor Yellow
    docker logs iris-api
    
    Write-Host "`n✅ API is running at: http://localhost:8000" -ForegroundColor Green
    Write-Host "✅ API Documentation: http://localhost:8000/docs" -ForegroundColor Green
    Write-Host "`nℹ️  To view logs: docker logs -f iris-api" -ForegroundColor Cyan
    Write-Host "ℹ️  To stop: docker stop iris-api" -ForegroundColor Cyan
} else {
    Write-Host "❌ Failed to start container" -ForegroundColor Red
}
