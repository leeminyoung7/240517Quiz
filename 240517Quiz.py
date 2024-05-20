def validation_of_resident_registration_number(a):
    a = a.replace("-", "")

    if len(a) != 13:
        return "잘못된 주민등록번호입니다."
    valid_check_code = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    total = 0
    for i in range(12):
        total += int(a[i]) * valid_check_code[i]

    check_digit = (11 - (total % 11)) % 10
    if check_digit == int(a[-1]):
        return "유효한 주민등록번호입니다."
    else:
        return "유효하지 않은 주민등록번호입니다."

resident_registration_number = input("주민등록번호를 입력하세요: ")
print(validation_of_resident_registration_number(resident_registration_number))