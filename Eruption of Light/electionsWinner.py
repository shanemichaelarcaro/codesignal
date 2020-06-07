def electionsWinners(votes, k):
    max_votes = max(votes)
    if k == 0:
        if votes.count(max_votes) > 1:
            return 0
    count = 0
    for vote in votes:
        if vote + k > max_votes:
            count += 1
    return count if count != 0 else 1


print(electionsWinners([2, 3, 5, 2], 3)) # => 2
print(electionsWinners([1, 3, 3, 1, 1], 0)) # => 0
print(electionsWinners([1, 1, 1, 1], 1)) # => 4
print(electionsWinners([5, 1, 3, 4, 1], 0)) # => 1
