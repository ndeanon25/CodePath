def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result

print(engagement_boost([-4, -1, 0, 3, 10])) #[0, 1, 9, 16, 100]
print(engagement_boost([-7, -3, 2, 3, 11])) # [4, 9, 9, 49, 121]