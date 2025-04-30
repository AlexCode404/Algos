def gray_to_binary(gray: int) -> int:
    binary = gray
    while gray > 0:
        gray >>= 1
        binary ^= gray
    return binary

class RotaryEncoder:
    def __init__(self, resolution_bits: int):
        self.max_count = 1 << resolution_bits

    def code_to_angle(self, gray_code: int) -> float:
        position = gray_to_binary(gray_code)
        return position / self.max_count * 360.0


encoder = RotaryEncoder(resolution_bits=8)
raw_gray = 0b11001010  # пример прочитанного кода
angle = encoder.code_to_angle(raw_gray)
print(f"Угол: {angle:.2f}°")
