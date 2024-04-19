sozler = {
        "LOL" : "komik bir şeye verilen cevap",
        "CRINGE" : "garip ya da utandırıcı bir şey",
        "ROFL" : "bir şakaya karşılık cevap",
        "SHEESH" : "onaylamamak",
        "CREEPY" : "korkunç",
        "AGGRO": "agresifleşmek/sinirlenmek",
}
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")        
if word in sozler.keys():
    print(word,"kelimesinin anlamı =",sozler[word])
else:
    print("bu kelime sözlükte mevcut değil ):")
    
