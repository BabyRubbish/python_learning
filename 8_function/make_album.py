def make_album(singer, name_of_album, amount=None):
    """制作专辑,记录歌手和唱片的名字,如果有数量的话也一并记录"""
    album = {}
    album["singer"] = singer.title()
    album["name_of_album"] = name_of_album.title()
    if amount:
        album["amount"] = amount
    return album


# albums = []
# albums.append(make_album("talor", "love story", 12))
# albums.append(make_album("jay zhou", "nunchakus"))
# albums.append(make_album("joker", "celestial alien", 10))

# for album in albums:
#     print(album)

albums = []

while True:
    print(f"Record the singer and the album!")
    print("(Enter 'q' at any time to quit!)")
    singer = input("Singer: ")
    if singer == "q":
        break

    album_name = input("Album: ")
    if singer == "q":
        break

    amount = input("Amount:")
    if singer == "q":
        break

    album = make_album(singer=singer, name_of_album=album_name, amount=amount)
    albums.append(album)

print("--- All the albums---")
for album in albums:
    print(album)
