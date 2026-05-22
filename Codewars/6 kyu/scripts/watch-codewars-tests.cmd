@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0watch-codewars-tests.ps1" %*
