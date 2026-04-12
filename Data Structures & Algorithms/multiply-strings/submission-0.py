class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = int(num1)
        num2_int = int(num2)
        if num1_int == 0 and num2_int == 0:
            return "0"

        result = num1_int * num2_int
        return str(result)
