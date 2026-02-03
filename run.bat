@echo off
REM RAG AI Assistant - Quick Start Script for Windows

echo.
echo ========================================
echo RAG AI Assistant - Setup & Run
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Checking dependencies...
pip list | findstr langchain >nul 2>&1
if errorlevel 1 (
    echo [2/4] Installing dependencies...
    pip install -r requirements.txt -q
    echo [2/4] Dependencies installed!
) else (
    echo [2/4] Dependencies already installed!
)

echo [3/4] Preparing documents...
python ingest.py
if errorlevel 1 (
    echo ERROR: Failed to ingest documents
    pause
    exit /b 1
)

echo [4/4] Starting FastAPI server...
echo.
echo ========================================
echo Server is running on: http://127.0.0.1:8000
echo API endpoint: http://127.0.0.1:8000/ask?q=your_question
echo ========================================
echo.

uvicorn app:app --reload --host 127.0.0.1 --port 8000

pause
