n = int(input())
arr = list(map(int, input().split()))

# Remove duplicates using set
unique_scores = list(set(arr))

# Sort in descending order
unique_scores.sort(reverse=True)


print(unique_scores[1])