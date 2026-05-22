@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0watch-codewars-autopush.ps1" %*
