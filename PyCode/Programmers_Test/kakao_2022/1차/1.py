def solution(today, terms, privacies):
    answer = []
    today = date_to_days(today)

    terms_dict = dict()
    for t in terms:
        t_s = t.split(' ')
        terms_dict[t_s[0]] = int(t_s[1])*28

    for i in range(len(privacies)):
        pp = privacies[i].split(' ')
        p_days = date_to_days(pp[0])
        p_terms = pp[1]

        if p_days + terms_dict[p_terms] <= today:
            answer.append(i+1)

    return answer


def date_to_days(date):
    d_splt = date.split('.')
    return int(d_splt[0])*336 + int(d_splt[1])*28 + int(d_splt[2])



print(solution('2022.05.19', ['A 6', 'B 12', 'C 3'], ['2021.05.02 A','2021.07.01 B', '2022.02.19 C', '2022.02.20 C']))