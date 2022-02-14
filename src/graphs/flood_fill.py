def flood_fill(image, sr, sc, new_color):
    if image[sr][sc] == new_color:
        return image
    old_color = image[sr][sc]
    image[sr][sc] = new_color
    if sr > 0 and image[sr - 1][sc] == old_color:
        flood_fill(image, sr - 1, sc, new_color)
    if sr < len(image) - 1 and image[sr + 1][sc] == old_color:
        flood_fill(image, sr + 1, sc, new_color)
    if sc > 0 and image[sr][sc - 1] == old_color:
        flood_fill(image, sr, sc - 1, new_color)
    if sc < len(image[0]) - 1 and image[sr][sc + 1] == old_color:
        flood_fill(image, sr, sc + 1, new_color)
    return image