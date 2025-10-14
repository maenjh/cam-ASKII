# 🎥 cam-ASKII

Real-time webcam to ASCII art converter built with Python.

[한국어](#한국어-korean) | [English](#english)

---

## English

### 📋 About

A Python project that converts live webcam feed into ASCII art in real-time. Two versions are available:

- **Terminal Version** (`webcam_ascii.py`): Displays ASCII art directly in the terminal
- **Streamlit Web App** (`app.py`): Web interface showing both original video and ASCII art side by side

### ✨ Features

- 🎬 Real-time webcam capture
- 🔡 Video to ASCII character conversion (`@%#*+=-:. `)
- 🎨 Customizable settings
  - ASCII width adjustment (80-200)
  - Font size control (8-20px)
  - Background and text color customization
- 📺 Side-by-side original video and ASCII art display (web app version)

### 🚀 Installation

#### Requirements

- Python 3.7 or higher
- Webcam-enabled device

#### Option 1: Using Conda (Recommended)

Create and activate a new conda environment:

```bash
# Create a new environment
conda create -n ascii-cam python=3.11

# Activate the environment
conda activate ascii-cam

# Install dependencies
pip install opencv-python numpy streamlit
```

#### Option 2: Using pip

```bash
pip install opencv-python numpy streamlit
```

or

```bash
pip install -r requirements.txt
```

### 💻 Usage

#### 1. Terminal Version

View ASCII art directly in your terminal.

```bash
cd pymid
python webcam_ascii.py
```

- Exit: `Ctrl + C`

#### 2. Streamlit Web App

Run the web interface for a more user-friendly experience.

```bash
cd pymid
streamlit run app.py
```

Your browser will automatically open with the following features:

- **Start/Stop buttons**: Control webcam capture
- **Sidebar settings**:
  - Adjust ASCII width
  - Control font size
  - Customize background and text colors

### 📁 Project Structure

```
cam-ASKII/
├── README.md
└── pymid/
    ├── app.py              # Streamlit web app version
    └── webcam_ascii.py     # Terminal version
```

### 🔧 Tech Stack

- **Python**: Main programming language
- **OpenCV**: Webcam capture and image processing
- **NumPy**: Efficient array operations
- **Streamlit**: Web interface framework

### 🎨 How It Works

1. Capture RGB frames from webcam
2. Convert to grayscale
3. Resize image (maintaining aspect ratio)
4. Map pixel brightness to ASCII characters
   - Dark pixels: `@`, `%`, `#`, etc.
   - Bright pixels: `:`, `.`, ` `, etc.
5. Convert to string and display

### 🐛 Troubleshooting

#### Cannot open webcam

- Check camera permissions
- Ensure no other program is using the webcam
- For macOS: System Preferences → Security & Privacy → Camera permissions

#### Slow frame rate

- Adjust `time.sleep(0.03)` value in `app.py`
- Reduce ASCII width (fewer characters = faster processing)

### 📝 License

Free to use for personal learning and research purposes.

### 🙏 Contributing

Bug reports and feature suggestions are always welcome!

---

## 한국어 (Korean)

### 📋 프로젝트 소개

실시간 웹캠 영상을 ASCII 아트로 변환하는 Python 프로젝트입니다. 두 가지 버전을 제공합니다:

- **터미널 버전** (`webcam_ascii.py`): 터미널에서 직접 ASCII 아트를 출력
- **Streamlit 웹앱 버전** (`app.py`): 웹 인터페이스로 원본 영상과 ASCII 아트를 동시에 확인

### ✨ 주요 기능

- 🎬 실시간 웹캠 영상 캡처
- 🔡 ASCII 문자로 영상 변환 (`@%#*+=-:. `)
- 🎨 커스터마이징 가능한 설정
  - ASCII 너비 조절 (80-200)
  - 폰트 크기 조절 (8-20px)
  - 배경색 및 문자색 변경
- 📺 원본 영상과 ASCII 아트 동시 표시 (웹앱 버전)

### 🚀 설치 방법

#### 필수 요구사항

- Python 3.7 이상
- 웹캠이 연결된 환경

#### 방법 1: Conda 사용 (권장)

새로운 conda 환경을 만들고 활성화합니다:

```bash
# 새 환경 생성
conda create -n ascii-cam python=3.11

# 환경 활성화
conda activate ascii-cam

# 패키지 설치
pip install opencv-python numpy streamlit
```

#### 방법 2: pip 사용

```bash
pip install opencv-python numpy streamlit
```

또는

```bash
pip install -r requirements.txt
```

### 💻 사용 방법

#### 1. 터미널 버전

터미널에서 직접 ASCII 아트를 확인할 수 있습니다.

```bash
cd pymid
python webcam_ascii.py
```

- 종료: `Ctrl + C`

#### 2. Streamlit 웹앱 버전

웹 브라우저에서 보다 편리하게 사용할 수 있습니다.

```bash
cd pymid
streamlit run app.py
```

웹 브라우저가 자동으로 열리며, 다음 기능들을 사용할 수 있습니다:

- **Start/Stop 버튼**: 웹캠 캡처 시작/중지
- **사이드바 설정**:
  - ASCII 너비 조절
  - 폰트 크기 조절
  - 배경색 및 문자색 커스터마이징

### 📁 프로젝트 구조

```
cam-ASKII/
├── README.md
└── pymid/
    ├── app.py              # Streamlit 웹앱 버전
    └── webcam_ascii.py     # 터미널 버전
```

### 🔧 기술 스택

- **Python**: 메인 프로그래밍 언어
- **OpenCV**: 웹캠 캡처 및 이미지 처리
- **NumPy**: 효율적인 배열 연산
- **Streamlit**: 웹 인터페이스 구축

### 🎨 ASCII 변환 원리

1. 웹캠에서 RGB 프레임 캡처
2. 그레이스케일(흑백)로 변환
3. 이미지 크기 조정 (가로세로 비율 유지)
4. 픽셀 밝기값을 ASCII 문자에 매핑
   - 어두운 픽셀: `@`, `%`, `#` 등
   - 밝은 픽셀: `:`, `.`, ` ` 등
5. 문자열로 변환하여 출력

### 🐛 문제 해결

#### 웹캠을 열 수 없습니다

- 카메라 권한을 확인하세요
- 다른 프로그램에서 웹캠을 사용 중인지 확인하세요
- macOS의 경우: 시스템 환경설정 → 보안 및 개인 정보 보호 → 카메라 권한 확인

#### 프레임이 느립니다

- `app.py`의 `time.sleep(0.03)` 값을 조절해보세요
- ASCII 너비를 줄여보세요 (더 적은 문자 = 더 빠른 처리)

### 📝 라이선스

이 프로젝트는 개인 학습 및 연구 목적으로 자유롭게 사용할 수 있습니다.

### 🙏 기여

버그 리포트나 기능 제안은 언제든 환영합니다!

---

**Made with ❤️ using Python, OpenCV, and Streamlit**
