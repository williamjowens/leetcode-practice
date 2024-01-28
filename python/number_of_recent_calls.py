"""
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

 

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
 

Constraints:

1 <= t <= 109
Each test case will call ping with strictly increasing values of t.
At most 104 calls will be made to ping.
"""

# Using a list
class RecentCounter(object):
    def __init__(self):
        self.recent_requests = []
        self.window = 3000
        
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # Add the new ping time
        self.recent_requests.append(t)
        
        # Remove pings that are older than t - window
        while self.recent_requests and self.recent_requests[0] <= t - self.window:
            self.recent_requests.pop(0)
        
        # Count the number of recent pings
        ping_count = len(self.recent_requests)
        
        return ping_count
    
# Test
recent_counter = RecentCounter()

ping_times = [1, 100, 3001, 3002, 3050]
for time in ping_times:
    count = recent_counter.ping(time)
    print(f"Time: {time}ms, Recent Pings: {count}")
    
    
# Using a deque
from collections import deque 

class RecentCounter(object):
    def __init__(self):
        self.recent_requests = deque()
        self.window = 3000 
        
    def ping(self, t):
        """ 
        :type t: int 
        :rtype: int 
        """
        # Add the new ping time
        self.recent_requests.append(t)
        
        # Remove pings that are older than t - window
        while self.recent_requests and self.recent_requests[0] <= t - self.window:
            self.recent_requests.popleft()
            
        # Count the number of recent pings
        ping_count = len(self.recent_requests)
        
        return ping_count
    
# Test
recent_counter = RecentCounter()

ping_times = [1, 100, 3001, 3002, 3050]
for time in ping_times:
    count = recent_counter.ping(time)
    print(f"Time: {time}ms, Recent Pings: {count}")