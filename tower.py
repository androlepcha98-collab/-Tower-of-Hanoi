
def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    result = []

    def record():
        result.append(" ".join(str(rod) for rod in rods))

    def move_disks(num, source, auxiliary, target):
        if num == 1:
            disk = rods[source].pop()
            rods[target].append(disk)
            record()
            return

        move_disks(num - 1, source, target, auxiliary)

        disk = rods[source].pop()
        rods[target].append(disk)
        record()

        move_disks(num - 1, auxiliary, source, target)

    record()
    move_disks(n, 0, 1, 2)

    return "\n".join(result)
