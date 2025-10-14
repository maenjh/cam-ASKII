import cv2
import numpy as np
import os
import time

# 아스키 문자를 밝기 순으로 정렬 (어두운 문자 -> 밝은 문자)
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """이미지 비율에 맞게 크기 조절"""
    (original_height, original_width) = image.shape
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width * 0.55) # 폰트 비율에 맞게 높이 조절
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

def gray_to_ascii(image):
    """흑백 이미지를 아스키 아트로 변환"""
    # 픽셀 값을 0과 len(ASCII_CHARS) - 1 사이의 인덱스로 변환
    intensity_matrix = (image / 255.0 * (len(ASCII_CHARS) - 1)).astype(int)
    
    # NumPy의 고급 인덱싱을 사용하여 아스키 문자로 빠르게 변환
    ascii_matrix = np.array(list(ASCII_CHARS))[intensity_matrix]
    
    # 각 행의 문자들을 합쳐서 문자열 리스트 생성
    ascii_lines = ["".join(row) for row in ascii_matrix]
    return "\n".join(ascii_lines)

def main():
    # 웹캠 열기
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("오류: 웹캠을 열 수 없습니다.")
        return

    try:
        while True:
            # 웹캠에서 프레임 읽기
            ret, frame = cap.read()
            if not ret:
                print("오류: 프레임을 읽을 수 없습니다.")
                break

            # 1. 흑백으로 변환
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # 2. 터미널 크기에 맞게 이미지 리사이즈
            resized_gray_frame = resize_image(gray_frame, new_width=120)
            
            # 3. 아스키 아트로 변환
            ascii_art = gray_to_ascii(resized_gray_frame)
            
            # 4. 화면을 지우고 아스키 아트 출력
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_art)
            
            # 프레임 간 약간의 딜레이 추가
            time.sleep(0.03)

            # 'q' 키를 누르면 종료 (OpenCV 창이 없으므로 터미널에서 Ctrl+C로 종료)
            # cv2.imshow를 사용하지 않으므로 waitKey가 동작하지 않음

    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")

    finally:
        # 웹캠 자원 해제
        cap.release()

if __name__ == "__main__":
    main()