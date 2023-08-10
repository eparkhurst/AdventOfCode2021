def inr(pos, arr):
	return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))

def bfs(ll):
    q = [(0, 0, 0)]
    costs = {}
    while True:
        cost,x,y = q[0]
        if x==len(ll)-1 and y==len(ll[0])-1: 
            print(cost)
            break
        q=q[1:]
        for xx,yy in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
            if inr((xx,yy),ll):
                nc = cost + ll[xx][yy]
                if (xx,yy) in costs and costs[(xx,yy)]<=nc:
                    continue
                costs[(xx,yy)]=nc
                q.append((nc,xx,yy))
        q = sorted(q)

def main():
    with open("input.txt") as f:
        input = f.read().strip().split("\n")
    risk = []
    for line in input:
        num_line = [int(x) for x in line]
        risk.append(num_line)
    bfs(risk)



if __name__ == "__main__":
    main()
# 717 too high