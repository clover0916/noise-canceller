import RPi.GPIO as GPIO

# GPIOのモードを設定（BCMモードを使用）
GPIO.setmode(GPIO.BCM)

# 入力ピンと出力ピンの定義
analog_input_pin = 17
output_pin = 18

# GPIOピンの設定
GPIO.setup(analog_input_pin, GPIO.IN)
GPIO.setup(output_pin, GPIO.OUT)

try:
    while True:
        # アナログ入力の読み取り
        analog_value = GPIO.input(analog_input_pin)

        # アナログ入力の反転
        inverted_value = not analog_value

        # 反転された値を出力
        GPIO.output(output_pin, inverted_value)

except KeyboardInterrupt:
    # Ctrl+Cが押されたら終了処理を行う
    GPIO.cleanup()
