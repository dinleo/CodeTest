def solution(record):
    answer = []
    seat = [['_', -1, 0, 0]]
    for r in record:
        person = r.split(' ')
        id = int(person[0][3:])
        cmd = person[1]
        if cmd == 'sit':
            k = int(person[2][2:])
            if len(seat) == 1:
                seat.append([id, k, k, k])
            else:
                new_seat = [id, '_', '_', k]
                for i in range(len(seat)):
                    space = seat[i][2] - seat[i][3]
                    if (k*2+1 <= seat[i][2]) and (k + 1 < space) and (seat[i-1][3] < space):
                        new_space = max(seat[i-1][3], k)
                        new_seat[1] = seat[i-1][1] + new_space + 1
                        new_seat[2] = new_space
                        seat[i][2] = seat[i][1] - new_seat[1] - 1
                        seat.insert(i, new_seat)
                        break
                if new_seat[1] == '_':
                    new_space = max(seat[-1][3], k)
                    new_seat[1] = seat[-1][1] + new_space + 1
                    new_seat[2] = new_space
                    seat.append(new_seat)
        else:
            for i in range(len(seat)):
                if seat[i][0] == id:
                    if i != len(seat) - 1:
                        seat[i+1][2] = seat[i+1][1] - seat[i-1][1] - 1
                    seat.pop(i)
                    break
    for s in seat:
        if s[0] != '_':
            answer.append([s[0], s[1]])


    return answer


print(solution(["id=1 sit k=1", "id=2 sit k=3", "id=3 sit k=2", "id=2 leave", "id=4 sit k=4", "id=5 sit k=2"]))
