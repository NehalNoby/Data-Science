def emoji_replacement(text):
    emoji_dict = {"happy":"😊","love":"❤️","cool":"😎","angry":"😠","confused":"😵‍💫","sad":"😔"}
    words = text.split()
    for word in words:
        if word in emoji_dict:
            text = text.replace(word, emoji_dict[word])
    return text
text=input("Enter your message: ")
print("Replaced Imoji:",emoji_replacement(text))
