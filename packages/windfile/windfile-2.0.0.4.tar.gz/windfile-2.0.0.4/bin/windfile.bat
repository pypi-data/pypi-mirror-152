@echo off
cd /d %~dp0
python -m windfile.fileman_ui %*
pause
