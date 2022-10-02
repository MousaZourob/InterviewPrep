class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        count_tasks = Counter(tasks)
        heap = []

        for count in count_tasks.values():
            heapq.heappush(heap, -count)

        elements = []

        while elements or heap:
            ans += 1
            if heap:
                count = heapq.heappop(heap) + 1
                if count < 0:
                    elements.append((count, ans + n))

            if elements and elements[0][1] == ans:
                heapq.heappush(heap, elements.pop(0)[0])

        return ans