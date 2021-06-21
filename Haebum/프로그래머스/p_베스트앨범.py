# 해시로 정렬 키:장르 벨류: 횟수, 고유번호
# 

def solution(genres, plays):
    answer = []
    songs = {}
    allGenres = {}
    for i in range(len(plays)):
        if songs.get(genres[i]):
            allGenres[genres[i]] += plays[i]
            songs[genres[i]].append([i,plays[i]])
        else:
            songs[genres[i]] = [[i,plays[i]]]
            allGenres[genres[i]] = plays[i]
    allGenres = sorted(allGenres.items(),key=lambda x : x[1],reverse=True)

    for g in allGenres:
        sorted_g = sorted(songs[g[0]], key=lambda x: x[1], reverse=True)
        answer.append(sorted_g[0][0])
        if len(sorted_g) > 1:
            answer.append(sorted_g[1][0])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 2500, 150, 800, 2500]
solution(genres, plays)