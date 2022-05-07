total_dictionary = {}

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_dictionary[question] = ""
print(total_dictionary)