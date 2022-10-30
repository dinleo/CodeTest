import req_solution as rs


def handle_request(auth_key, hotel, req_stack, res_stack, day, problem):
    req = []
    reply_arr = []
    max_day = len(req_stack)
    if problem == 1:
        for d in range(day, min(day + 13, max_day)):
            for s in req_stack[d]:
                if s['check_in_date'] < day + 7:
                    req.append(s)
                elif 7 <= s['amount']:
                    req.append(s)
    else:
        for d in range(day, min(day + 21, max_day)):
            for s in req_stack[d]:
                req.append(s)
    req.sort(reverse=True, key=lambda x: x['amount'])

    for r in req:
        room_num = find_room_pos(hotel, r['check_in_date'], r['amount'])
        if room_num != 0:
            reply_arr.append({'id': r['id'], 'reply': 'accepted'})
            res_stack[r['check_in_date']].append({'id': r['id'], 'room_number': room_num})
            reservation(hotel, r['check_out_date'], room_num, r['amount'])
        else:
            reply_arr.append({'id': r['id'], 'reply': 'refused'})
        remove_req_stack(req_stack, r['id'], day)

    rs.reply(auth_key, reply_arr)


def find_room_pos(hotel, day, amount):
    empty_count = count_empty_room(hotel, day)
    for i in range(len(hotel)):
        if empty_count[i] < amount:
            continue
        j = 0
        while j + amount <= len(hotel[i]):
            if hotel[i][j] <= day:
                start = j
                pos = True
                for a in range(amount - 1):
                    j += 1
                    if day < hotel[i][j]:
                        pos = False
                        break
                if pos:
                    return (i + 1) * 1000 + (start + 1)
            else:
                j += 1
    return 0


def remove_req_stack(stack, id, start_day):
    for i in range(start_day, start_day + 21):
        for j in range(len(stack[i])):
            if stack[i][j]['id'] == id:
                del stack[i][j]
                return True
    return False


def reservation(hotel, day, room_num, amount):
    room_num = str(room_num)
    floor = int(room_num[:-3]) - 1
    num = int(room_num[-3:]) - 1
    for i in range(num, num + amount):
        hotel[floor][i] = day


def count_empty_room(hotel, day):
    floor = len(hotel)
    count = [0 for _ in range(floor)]
    for i in range(floor):
        for j in hotel[i]:
            if j <= day:
                count[i] += 1
    return count


def stack_req(auth_key, stack, today):
    req = rs.get_new_req(auth_key)
    for r in req:
        stack[min(today + 14, r['check_in_date'] - 1)].append(r)
