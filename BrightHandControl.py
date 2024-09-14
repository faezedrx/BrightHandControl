import cv2
import mediapipe as mp
import os

# تابع تنظیم نور صفحه
def set_brightness(level):
    # مقدار سطح روشنایی باید بین 0 و 100 باشد
    brightness = max(0, min(100, level))
    os.system(f'powershell.exe -ExecutionPolicy Bypass -File ./set_brightness.ps1 -brightness {brightness}')

# تنظیمات Mediapipe برای تشخیص دست
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# راه‌اندازی دوربین
cap = cv2.VideoCapture(0)

# تنظیمات اولیه Mediapipe
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # تبدیل تصویر به RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        # پردازش تصویر برای شناسایی دست
        results = hands.process(image)
        image.flags.writeable = True
        
        # برگرداندن تصویر به BGR برای نمایش
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # اگر دستی شناسایی شد
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # نقاط کلیدی انگشتان
                thumb_tip = hand_landmarks.landmark[4]
                index_tip = hand_landmarks.landmark[8]
                middle_tip = hand_landmarks.landmark[12]
                ring_tip = hand_landmarks.landmark[16]
                pinky_tip = hand_landmarks.landmark[20]
                
                # محاسبه فاصله بین نوک انگشت شست و نوک انگشت اشاره
                distance_thumb_index = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5
                
                # محاسبه درصد باز بودن دست
                num_fingers_open = sum([thumb_tip.y < index_tip.y + 0.1,
                                        index_tip.y < middle_tip.y + 0.1,
                                        middle_tip.y < ring_tip.y + 0.1,
                                        ring_tip.y < pinky_tip.y + 0.1])
                
                if distance_thumb_index < 0.05:  # اگر انگشتان نزدیک هم هستند، دست بسته است
                    brightness_level = 0
                else:
                    # درصد روشنایی بر اساس تعداد انگشتان باز شده
                    brightness_level = max(0, min(100, (num_fingers_open / 5) * 100))
                
                set_brightness(brightness_level)
        
        # نمایش تصویر پردازش شده
        cv2.imshow('Hand Detection', image)
        
        # خروج با فشردن کلید 'q'
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# آزاد کردن منابع
cap.release()
cv2.destroyAllWindows()
