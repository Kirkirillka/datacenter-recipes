# Download Telegraf Agent
Invoke-WebRequest -Uri "https://dl.influxdata.com/telegraf/releases/telegraf-1.11.1_windows_amd64.zip" -outfile "$env:TEMP/telegraf-1.11.1_windows_amd64.zip"
Expand-Archive   "$env:TEMP/telegraf-1.11.1_windows_amd64.zip" "$env:TEMP/telegraf-1.11.1_windows_amd64"

# Move into file direcotry
Move-Item -Path "$env:TEMP/telegraf-1.11.1_windows_amd64"  -Destination "C:/Program Files/telegraf"

# Also copy config
Copy-Item -Path "telegraf.conf"  -Destination "C:/Program Files/telegraf/telegraf.conf"


# Must be ran under Administrator to install Telegraf as a service

& 'C:\Program Files\telegraf\telegraf.exe' -service install