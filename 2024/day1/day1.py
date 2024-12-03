import pandas as pd

# Part1
df = pd.read_csv("./2024/day1/input.txt", names=["left", "right"],sep='\s+')
print(df.head())
left_sorted = df['left'].sort_values().reset_index(drop=True)
right_sorted= df['right'].sort_values().reset_index(drop=True)
print(left_sorted)
print(right_sorted)
distance = abs(right_sorted-left_sorted)
total_distance= distance.sum()
print(total_distance)

# Part2
similarity_score=0
for i in left_sorted:
    count=0
    for j in right_sorted:
        if i==j:
            count+=1
    
    similarity_score += i*count

print(similarity_score)