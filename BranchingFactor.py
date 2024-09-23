def branching_factor(depth, nodes, tolerance, max_iterations):
    b = 2.0 
    for _ in range(max_iterations):
        estimate = (1-b**(depth+1))/(1-b) - 1 - nodes
        # estimate = (b**(depth+1) - 1) / (b - 1) - nodes
        print(b, estimate)
        if abs(estimate) < tolerance:
            return b
        b -= estimate/(((depth*b-depth-1)*(b**depth)+1)/((b-1)**2))
        # b -= estimate/(((b - 1) * (depth+1) * b**depth - (b**(depth+1) - 1)) / (b - 1)**2)
    print("Error: Max Iterations Reached")
    return b


def main():
    pass


if __name__ == "__main__":
    main()