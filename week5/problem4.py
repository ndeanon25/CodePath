def average_nft_value(nft_collection):
    if not nft_collection:   #Check if its empty 
        return 0

    for i in nft_collection:
        totalnftValues = sum(nft_collection)

    return len(nft_collection)
    

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection)) # 5.7

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2)) #9.15

nft_collection_3 = []
print(average_nft_value(nft_collection_3)) # 0
