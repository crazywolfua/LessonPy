# def count_sum(count, param):
#     result = 0
#     if param == "even":
#         for i in range(0, count + 1, 2):
#             result += i
#     if param == "odd":
#         for i in range(1, count + 1, 2):
#             result += i
#     print(result)
#
# count = int(input("Введите число: "))
# param = input("Введите значение: ")
#
# count_sum(count, param)


def validate_password(passw):

    if len(passw) < 5 :
        return False

    def count_upper_case(passw):
        count_upper = sum(1 for char in passw if char.isupper())
        if count_upper < 2:
            return False

    def digits_exists(passw):
        count_digits = sum(1 for char in passw if char.isdigit())
        if count_digits == 0:
            return False

    if count_upper_case(passw) is False or digits_exists(passw) is False:
        return False
    return True


print(validate_password(input("Введите пароль: ")))
