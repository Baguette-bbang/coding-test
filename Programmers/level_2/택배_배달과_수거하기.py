def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries or pickups:
        
        while deliveries and deliveries[-1]==0:
            deliveries.pop()
        while pickups and pickups[-1]==0:
            pickups.pop()
            
        dist = 0
        dist = len(deliveries)
        delivery_cap = 0
        
        while deliveries and delivery_cap < cap:
            if deliveries[-1] + delivery_cap <= cap:
                delivery_cap += deliveries[-1]
                deliveries.pop()
            else:
                deliveries[-1] -= cap - delivery_cap
                delivery_cap = cap
                
        dist = max(dist, len(pickups))
        pickup_cap = 0
        while pickups and pickup_cap < cap:
            if pickups[-1] + pickup_cap <= cap:
                pickup_cap += pickups[-1]
                pickups.pop()
            else:
                pickups[-1] -= cap - pickup_cap
                pickup_cap = cap
                
        answer += dist*2
        print(deliveries, pickups)
    return answer