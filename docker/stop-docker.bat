@echo off
setlocal

echo Stopping esphome container...
docker compose stop esphome-usb
docker compose stop esphome-ota

