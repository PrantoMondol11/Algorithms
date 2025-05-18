jobs = [[1, 2, 100], [2, 1, 50], [3, 2, 10], [4, 1, 20], [5, 3, 30]]  # [job_id, deadline, profit]

# Sort jobs by profit descending
jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

max_deadline = max(job[1] for job in jobs)
slots = [False] * (max_deadline + 1)  # time slots, index 1-based
answer = []

for job_id, deadline, profit in jobs:
    for t in range(deadline, 0, -1):  # try to assign latest possible slot
        if not slots[t]:
            slots[t] = True
            answer.append([job_id, t, profit])  # job_id, slot, profit
            break

# Output result
for job in answer:
    print("Job:", job[0], "→ Slot:", job[1], "→ Profit:", job[2])
