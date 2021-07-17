def solution(genres, plays):
    genre = {}
    answer = []
    for g in genres:
        genre[g]=[0,[]]
    for idx, g in enumerate(genres):
        genre[g][0]+=plays[idx]
        genre[g][1].append([plays[idx],idx])
    genre = sorted(genre.values(),reverse=True)
    for v in genre:
        nG = sorted(v[1],key=lambda x:(-x[0],x[1]))
        for i,n in enumerate(nG):
            if i>1:
                break
            answer.append(n[1])
    
    return answer
