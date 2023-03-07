from random import randint

# Create Stream - Extract
stream = []
for _ in range(222):
    # roll three dice to generate a normal population
    stream.append(randint(1, 6) + randint(1, 6) + randint(1, 6))
print(stream)

# Create Aggregate Count - Transform
aggregate = {}
for n in range(3, 19):  # initialize all counts to 0
    aggregate[n] = 0
for n in stream:  # process stream
    aggregate[n] = aggregate[n] + 1

# Show Chart - Load
for k, v in aggregate.items():
    print(f'{v:2} {k:2} | {"X" * v}')
