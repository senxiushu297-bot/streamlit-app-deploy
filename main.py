# リストから偶数だけを抽出する関数
def extract_even_length_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# 関数「extract_even_numbers」に要素数が10のリストを渡して、戻り値のリストの合計値と平均値を計算して表示する
if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = extract_even_length_numbers(input_list)
    
    total = sum(even_numbers)
    average = total / len(even_numbers) if even_numbers else 0
    
    print(f"Even numbers: {even_numbers}")
    print(f"Total: {total}")
    print(f"Average: {average}")

# 数値のリストを受け取り、各値に基づいてカテゴリを分類する関数を作成してください

# 条件:

# 1. 値が0以下の場合は "Low" カテゴリに分類してください

# 2. 値が1以上10以下の場合は "Medium" カテゴリに分類してください

# 3. 値が10を超える場合は "High" カテゴリに分類してください

# 4. 入力リストには整数が含まれるものとします

# 結果を辞書形式で返してください。キーがカテゴリ名で、値が該当する数値のリストとします
def categorize_numbers(numbers):
    categories = {
        "Low": [],
        "Medium": [],
        "High": []
    }
    for num in numbers:
        if num <= 0:
            categories["Low"].append(num)
        elif 1 <= num <= 10:
            categories["Medium"].append(num)
        else:
            categories["High"].append(num)
    return categories

def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be positive")
    bmi = weight / (height ** 2)
    return bmi

# BMIを計算する関数

# BMIを表示してから戻り値を返す

def calculate_bmi_and_print(weight, height):
    bmi = calculate_bmi(weight, height)
    print(f"BMI: {bmi:.2f}")
    return bmi

