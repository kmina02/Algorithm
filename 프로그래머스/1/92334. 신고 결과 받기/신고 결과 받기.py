def solution(id_list, report, k):
    reported = {}
    mail = {}
    for i in id_list:
        mail[i] = 0
        reported[i] = []
        
    for r in set(report):
        id1, id2 = r.split(" ")        
        reported[id2].append(id1)
    
    for i in id_list:
        if len(reported[i]) >= k:
            for id in reported[i]:
                mail[id] += 1

    return list(mail.values())