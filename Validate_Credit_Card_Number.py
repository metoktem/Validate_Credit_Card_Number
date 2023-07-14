print("-" * 60)
print("Bu programda kredi kartınızı doğrulayabilirsiniz.")
print("-" * 60)

def validate_card_number(card_number):
        total = 0
        card_length = len(card_number)
        if card_length == 16:  # Visa / Master Card için doğrulama
            for i in range(card_length):
                if i % 2 == 0:
                    digit = int(card_number[i])
                    doubled_digit = digit * 2
                    if doubled_digit >= 10:
                        total += doubled_digit // 10 + doubled_digit % 10
                    else:
                        total += doubled_digit
                else:
                    total += int(card_number[i])

            if total % 10 == 0:
                return "Girdiğiniz kredi kartı geçerli bir Visa/Master kartıdır."
            else:
                return "Girdiğiniz kredi kartı geçersizdir."

        elif card_length == 15:  # American Ekspress Card için doğrulama
            for i in range(card_length):
                if i % 2 == 1:
                    digit = int(card_number[i])
                    doubled_digit = digit * 2
                    if doubled_digit >= 10:
                        total += doubled_digit // 10 + doubled_digit % 10 # Kart numarası 2 ile çarpıldığında çift haneli değer geldiğinde değerler ayrı ayrı alınır.
                    else:
                        total += doubled_digit
                else:
                    total += int(card_number[i])

            if total % 10 == 0:
                return "Girdiğiniz kredi kartı geçerli bir American Ekspress kartıdır."
            else:
                return "Girdiğiniz kredi kartı geçersizdir."

        elif card_length == 14 and (card_number.startswith(("36" , "305" , "300" , "38" , "39"))):  # Diner Card için doğrulama
            for i in range(card_length):
                if i % 2 == 0:
                    digit = int(card_number[i])
                    doubled_digit = digit * 2
                    if doubled_digit >= 10:
                        total += doubled_digit // 10 + doubled_digit % 10
                    else:
                        total += doubled_digit
                else:
                    total += int(card_number[i])

            if total % 10 == 0: # Kredi Kart Kontrol işlemlerinde total değerin 10'a bölümü 0 olmalıdır.
                return "Girdiğiniz kredi kartı geçerli bir Diners Club kartıdır."
            else:
                return "Girdiğiniz Diners Club kart numarası geçersizdir"

        else:
            return "Girdiğiniz Kredi Kart Numarası geçersizdir"
        
while True: # Tekrarlı kontrol için while döngüsüne sokulmuştur.
    card_number = input("Lütfen Kredi Kart Numaranızı giriniz (Çıkmak için 'exit' yazınız): ")
    card_number = card_number.replace(" ", "") # Kullanıcı Kredi Kart numarasını kontrol ederken boşluk koyabilir.        
    if card_number.lower() == "exit" or card_number == "EXİT" or card_number == "exıt": # Farklı varyasyonlarda exit yazıldığında döngü sonlanır.
        print("Kredi Kartı Kontrol işlemi sonlanmıştır.")
        break    
    result = validate_card_number(card_number)
    print(result)