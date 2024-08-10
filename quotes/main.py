# відкриваємо для читання

with open("quotes.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(line)

answer = input("Хто написав ці рядки?")
#Відкриваємо дозапису
with open("quotes.txt", "r", encoding="UTF-8") as file:
    file.write("\n",answer)

while True:
    #Запитуємо в автора чи він хоче додати цитату
    answer = input("Бажаєто додати ще одну цитату? (так \ ні)")  
    answer = answer.lower()

    if answer == "так":
        quote = input("Введіть цитату:")
        author = input("Введіть автора:")
        with open("quotes.txt", "r", encoding="UTF-8") as file:
            file.write("\n",quote )
            file.write("\n",author )
            file.close()
    else:
        break

with open("quotes.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(line)